from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from data.progress import get_user_progress
from data.shared import courses, course_titles, main_menu_keyboard  # Імпортуємо courses
import logging

router = Router()


# Клавіатура для вибору ролі користувача
role_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👨‍🏫 Я — вчитель")],
        [KeyboardButton(text="🎓 Я — учень")],
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def cmd_start(message: Message):
    # Вітальне повідомлення та вибір ролі
    await message.answer(
        "👋 Привіт! Я бот, який допоможе тобі пройти курс \"Основи роботи з mozaBook та mozaWeb\".\n\n"
        "Спочатку обери, хто ти:",
        reply_markup=role_keyboard
    )

@router.message(lambda msg: msg.text in ["👨‍🏫 Я — вчитель", "🎓 Я — учень"])
async def set_role(message: Message):
    # Збереження ролі користувача (учень/вчитель)
    role = "вчитель" if "вчитель" in message.text else "учень"
    # Тут можна зберегти роль у БД
    await message.answer(f"Твоя роль збережена як <b>{role}</b>. Обери дію нижче:", reply_markup=main_menu_keyboard)

@router.message(F.text == "📊 Мій прогрес")
async def show_progress(message: Message):
    # Вивід прогресу користувача по всіх курсах та модулях
    user_id = message.from_user.id
    user_data = get_user_progress(user_id)

    response = "<b>📊 Ваш прогрес:</b>\n\n"

    for course_id, course_info in courses.items():
        response += f"📘 <b>{course_info['title']}</b>\n\n"
        user_course = user_data["courses"].get(course_id, {})
        user_modules = user_course.get("modules", {})

        for module_id, module_info in course_info["modules"].items():
            user_module_data = user_modules.get(module_id, {"completed": False, "test_score": 0.0})
            status_emoji = "✅" if user_module_data["completed"] else "❌"
            score = user_module_data["test_score"]

            response += (
                f"🔹 <b>{module_info['title']}</b>\n"
                f"  Статус: {status_emoji} {'Завершено' if user_module_data['completed'] else 'Не завершено'}\n"
                f"  Результат тесту: {score:.2f}%\n\n"
            )

    await message.answer(response.strip(), parse_mode="HTML")

