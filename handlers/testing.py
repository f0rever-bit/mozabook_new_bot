from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.start import main_menu_keyboard
from data.quiz_data import quiz_questions
from data.shared import courses
from data import progress
import logging

router = Router()

# Стан машини для тестування: вибір модуля, проходження тесту
class QuizState(StatesGroup):
    module_selected = State()
    answering = State()

# Словник: назва модуля -> (course_key, module_index)
module_name_to_index_map = {}
for course_key, course_data in courses.items():
    module_titles = list(course_data["modules"].keys())
    for index, module_title in enumerate(module_titles):
        module_name_to_index_map[module_title] = (course_key, index)

# Клавіатура для вибору модуля для тесту
def module_keyboard():
    buttons = []
    for course_key, course_data in courses.items():
        module_titles = list(course_data["modules"].keys())
        for index, module_title in enumerate(module_titles):
            callback_data = f"start_quiz:{course_key}:{index}"
            buttons.append([InlineKeyboardButton(text=module_title, callback_data=callback_data)])
    buttons.append([InlineKeyboardButton(text="🏠 Меню", callback_data="to_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Клавіатура для вибору відповіді на питання тесту
def question_keyboard(module, question_index):
    question = quiz_questions[module]["questions"][question_index]
    options = question["options"]
    buttons = [
        [InlineKeyboardButton(text=opt, callback_data=f"quiz_answer:{module}:{question_index}:{i}")]
        for i, opt in enumerate(options)
    ]
    buttons.append([InlineKeyboardButton(text="🔚 Завершити тест", callback_data="end_quiz")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Старт тестування: показати список модулів
@router.message(F.text == "📝 Пройти тестування")
async def show_module_list(message: Message, state: FSMContext):
    await state.clear()

    response = "📘 <b>Оберіть модуль для проходження тесту:</b>\n"
    buttons = []

    for course_key, course_data in courses.items():
        for module_id, module_data in course_data["modules"].items():
            buttons.append([InlineKeyboardButton(text=module_data["title"], callback_data=f"quiz_module:{module_id}")])

    buttons.append([InlineKeyboardButton(text="🏠 Меню", callback_data="to_menu")])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer(response, parse_mode="HTML", reply_markup=keyboard)

# Початок тесту для модуля (через вибір модуля)
@router.callback_query(F.data.startswith("quiz_module:"))
async def start_quiz_module(callback: CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()
    except Exception:
        pass
    module_id = callback.data.split(":")[1]

    # Визначаємо course_key за module_id
    course_key = None
    for c_key, c_data in courses.items():
        if module_id in c_data["modules"]:
            course_key = c_key
            break

    if not course_key:
        await callback.message.answer("❗️Не вдалося визначити курс для цього модуля.")
        return

    await state.set_data({"module_id": module_id, "course_key": course_key, "index": 0, "score": 0})
    await send_question(callback.message, state)

# Початок тесту для модуля (через кнопку в модулі)
@router.callback_query(F.data.startswith("start_quiz:"))
async def start_quiz(callback: CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()
    except Exception:
        pass
    _, course_key, module_index = callback.data.split(":")
    module_index = int(module_index)
    module_id = list(courses[course_key]["modules"].keys())[module_index]

    logging.info(f"Starting quiz: user_id={callback.from_user.id}, course_key={course_key}, module_id={module_id}")

    await state.update_data(module_id=module_id, course_key=course_key, score=0, index=0)
    await send_question(callback.message, state)

# Відправка питання користувачу
async def send_question(message: Message, state: FSMContext):
    data = await state.get_data()
    module_id = data.get("module_id")
    index = data.get("index", 0)

    if not module_id or module_id not in quiz_questions:
        await message.answer("❌ Помилка: модуль не знайдено.")
        return

    questions = quiz_questions[module_id]["questions"]

    if index >= len(questions):
        score = data.get("score", 0)
        course_key = data.get("course_key", "")
        user_id = message.chat.id

        progress.update_module_progress(user_id, course_key, module_id)
        progress.update_test_score(user_id, course_key, module_id, round(score / len(questions) * 100, 2))

        await state.clear()
        await message.answer(
            f"🎉 Ви завершили тест!\nПравильних відповідей: <b>{score} з {len(questions)}</b>",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="🏠 Повернутись у меню", callback_data="to_menu")]]
            )
        )
        return

    question = questions[index]
    text = f"<b>{question['question']}</b>"
    await message.answer(text, parse_mode="HTML", reply_markup=question_keyboard(module_id, index))

# Обробка відповіді користувача на питання тесту
@router.callback_query(F.data.startswith("quiz_answer:"))
async def handle_answer(callback: CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()
    except Exception:
        pass
    _, module, index_str, selected_index_str = callback.data.split(":", 3)
    index = int(index_str)
    selected_index = int(selected_index_str)

    question = quiz_questions[module]["questions"][index]
    correct = question["answer"]
    selected_option = question["options"][selected_index]

    data = await state.get_data()
    score = data.get("score", 0)

    logging.info(f"Answer received: user_id={callback.from_user.id}, module={module}, index={index}, selected={selected_option}, correct={correct}")

    if selected_option == correct:
        score += 1
        await callback.message.answer("✅ Правильно!")
    else:
        await callback.message.answer("❌ Неправильно.")

    await state.update_data({"score": score, "index": index + 1})
    await send_question(callback.message, state)

# Завершення тесту достроково
@router.callback_query(F.data == "end_quiz")
async def end_quiz(callback: CallbackQuery, state: FSMContext):
    # Не видаляємо повідомлення з результатом тесту
    data = await state.get_data()
    score = data.get("score", 0)
    module = data.get("module_id", "")
    course = data.get("course_key", "")
    total = len(quiz_questions.get(module, {}).get("questions", []))
    user_id = callback.from_user.id

    progress.update_module_progress(user_id, course, module)
    progress.update_test_score(user_id, course, module, round(score / total * 100, 2))

    await state.clear()
    await callback.message.answer(
        f"📊 Тест завершено.\nПравильних відповідей: <b>{score} з {total}</b>",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="🏠 Повернутись у меню", callback_data="to_menu")]]
        )
    )

# Повернення у головне меню
@router.callback_query(F.data == "to_menu")
async def return_to_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await callback.message.delete()
    except Exception:
        pass
    await callback.message.answer("🔙 Ви повернулись у головне меню.", reply_markup=main_menu_keyboard)
