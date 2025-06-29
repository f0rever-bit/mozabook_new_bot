from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Загальні змінні
course_titles = {
    "course1": "Основи роботи з mozaBook та mozaWeb",
    "course2": "Використання Mozaik у дистанційній освіті",
}

# Головне меню (українською)
main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📘 Почати/Продовжити навчання")],
        [KeyboardButton(text="📝 Пройти тестування")],
        [KeyboardButton(text="❓ Часті питання (FAQ)")],
        [KeyboardButton(text="📊 Мій прогрес")],
        [KeyboardButton(text="❗ Технічна підтримка")],
    ],
    resize_keyboard=True
)

courses = {
    "course1": {
        "title": "Основи роботи з mozaBook та mozaWeb",
        "modules": {
            "module1": {
                "title": "Перші кроки в системі Mozaik",
                "summary": [
                    "Огляд системи Mozaik: mozaBook та mozaWeb.",
                    "Типи активаційних кодів.",
                    "Реєстрація, встановлення програми та створення акаунту.",
                    "Основні налаштування профілю та робота з медіатекою."
                ],
                "description": """
Mozaik Education — це комплексне освітнє рішення від угорської компанії Mozaik, що поєднує у собі програму mozaBook (встановлюється на ПК з ОС Windows) та онлайн-портал mozaWeb (доступний через браузер). MozaBook призначена для створення та демонстрації цифрових уроків, з використанням медіаелементів, інтерактивних інструментів, симуляцій і цифрових підручників. mozaWeb, у свою чергу, дозволяє переглядати готові матеріали, працювати з підручниками, 3D-сценами, відео та іншими ресурсами онлайн.

Існує кілька типів активаційних кодів:
• mozaBook Classroom+ — надає доступ до програми на одному пристрої з великим екраном (інтерактивна панель, проєктор), дозволяє створювати уроки, використовувати всю медіатеку та завантажувати презентації до хмари.
• mozaBook SchoolLab+ — один пристрій, використовується почергово кількома учнями або вчителями.
• mozaWeb Student — активує акаунт користувача незалежно від пристрою, з доступом до більшості функцій.
"""
            },
            "module2": {
                "title": "Робота з документами у програмі mozaBook",
                "summary": [
                    "Створення, відкриття, редагування та збереження зошитів.",
                    "Імпорт документів.",
                    "Робота з текстом, таблицями, зображеннями."
                ],
                "description": """
У mozaBook користувач може створити новий зошит (аналог цифрової книги або презентації) для підготовки уроків. Зошит зберігається локально або в хмарі, доступний для перегляду на інших пристроях через акаунт. Підтримується імпорт форматів PDF, PPT, PPTX, IWB, CFF. Імпортовані сторінки автоматично конвертуються у слайди.

Функції редагування включають:
• Вставку тексту (з можливістю вибору шрифтів, кольору, розміру).
• Малювання (олівець, маркер, фігури). Маркер дозволяє виділяти або підкреслювати важливу інформацію на сторінці.
• Роботу з таблицями (вставка, форматування, обчислення через інструмент "Вставка таблиці").
• Вставку мультимедіа: відео, аудіо, 3D-сцен, посилань.
• Додавання інтерактивних елементів: вікторини, завдання, анімації.
• Збереження в PDF або у форматі mozaBook.
"""
            },
            "module3": {
                "title": "Можливості роботи з вмістом у програмі mozaBook",
                "summary": [
                    "Інтеграція мультимедійного вмісту у зошити.",
                    "Медіатека: 3D-сцени, відео, анімації, картинки.",
                    "Вікторини, симуляції, інструменти для практики."
                ],
                "description": """
mozaBook дозволяє додавати інтерактивні матеріали до кожного слайду зошита. Це значно підвищує ефективність навчання. Медіатека — основне джерело цифрового вмісту, який можна фільтрувати за предметами або віком. Підключення до мережі обов’язкове для завантаження вмісту з медіатеки.

Доступні типи вмісту:
• 3D-сцени: дозволяють вивчати об’єкти з різних ракурсів, доступні анімації, текстові коментарі. Для першого запуску необхідно встановити спеціальний плеєр.
• Відео: освітні ролики з субтитрами українською, зручне керування переглядом.
• Інструменти: цифрові лінійки, калькулятори, лабораторії.
• Ігри: тренують памʼять, логіку, швидкість реакції, сприяють гейміфікації навчання.
"""
            },
            "module4": {
                "title": "Інтерактивне наповнення у програмі mozaBook",
                "summary": [
                    "Створення насичених уроків з мультимедіа.",
                    "Вбудовування вікторин, тестів, симуляцій."
                ],
                "description": """
Цей модуль демонструє, як зробити урок візуально привабливим і залучити учнів до активної участі. mozaBook підтримує інтерактивне середовище, де кожен слайд може включати 3D-сцену, відео, зображення, аудіо, текстові блоки, вправи. Використання вкладок з вікторинами дозволяє оцінювати знання учнів в реальному часі автоматично.

Учитель має змогу:
• Створити тести з варіантами відповідей.
• Використовувати елементи гейміфікації.
• Поєднувати різні типи контенту в одному уроці на одному слайді (наприклад: текст + 3D-сцена + вікторина).
"""
            },
            "module5": {
                "title": "Використання цифрових підручників у програмі mozaBook",
                "summary": [
                    "Завантаження та навігація цифровими підручниками.",
                    "Інтеграція підручника до зошита.",
                    "Робота з інтерактивним вмістом у підручниках."
                ],
                "description": """
mozaBook підтримує українські цифрові підручники. Користувач може відкрити будь-який підручник із бібліотеки, швидко переходити між сторінками за допомогою інтерактивного змісту або активних посилань, запускати пов’язаний цифровий вміст: 3D-сцени, відео, вікторини. Всі активні елементи розміщені на полях сторінки.

Підручник можна:
• Переглядати у повноекранному режимі, що покращує читабельність та зосередженість учня.
• Робити позначки, коментарі.
• Вставляти сторінки підручника у власний зошит за допомогою кнопки "Вставити в зошит".
• Використовувати як основу для створення уроків.
"""
            }
        }
    },
    "course2": {
        "title": "Використання Mozaik у дистанційній освіті",
        "modules": {
            "module6": {
                "title": "Загальні поняття про систему Mozaik",
                "summary": [
                    "Огляд освітньої системи Mozaik.",
                    "Створення та приєднання до освітнього закладу.",
                    "Зміна назви освітнього закладу.",
                    "Алгоритм встановлення статусу «Вчитель».",
                    "Форми дистанційної освіти з Mozaik."
                ],
                "description": """
Система Mozaik — це інтерактивна освітня платформа, яка включає програми mozaBook та mozaWeb. Вона дозволяє створювати та проводити уроки з використанням цифрових підручників, 3D-сцен, відео та інтерактивних інструментів.
"""
            },
            "module7": {
                "title": "Формування класу в системі Mozaik",
                "summary": [
                    "Різниця між правами учня та вчителя.",
                    "Коди активації.",
                    "Реєстрація учнів.",
                    "Формування класу/групи."
                ],
                "description": """
У системі Mozaik вчителі та учні мають різні рівні доступу. Вчителі можуть створювати та редагувати навчальні матеріали, тоді як учні мають доступ до перегляду та виконання завдань.
"""
            },
            "module8": {
                "title": "Планування дистанційного уроку",
                "summary": [
                    "Приклад плану уроку.",
                    "Типові помилки та рекомендації."
                ],
                "description": """
Планування дистанційного уроку в Mozaik включає визначення теми, цілей, підбір відповідних матеріалів (3D-сцен, відео, інтерактивних завдань) та створення структури уроку. Важливо враховувати рівень підготовки учнів та забезпечити доступність матеріалів.
"""
            },
            "module9": {
                "title": "Підготовка матеріалів у mozaBook",
                "summary": [
                    "Вибір шаблону.",
                    "Створення слайдів з текстом, медіа.",
                    "Вставка завдань."
                ],
                "description": """
У програмі mozaBook вчитель може створювати повноцінні інтерактивні уроки. Для цього обирається шаблон, створюються слайди з текстовим та візуальним наповненням, додаються відео, 3D-сцени, вікторини, тести та інструменти.
"""
            },
            "module10": {
                "title": "Проведення онлайн-уроку та комунікація",
                "summary": [
                    "Демонстрація уроку онлайн.",
                    "Застосування відеоконференцій.",
                    "Зворотний зв'язок і ДЗ."
                ],
                "description": """
Після створення уроку вчитель може провести його онлайн — демонструючи матеріали через спільний доступ до екрана у відеоконференцсервісах (Zoom, Google Meet тощо). Платформа mozaWeb дозволяє поширювати зошити серед учнів для самостійного вивчення або перегляду в асинхронному режимі.
"""
            }
        }
    }
}


main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📘 Почати/Продовжити навчання")],
        [KeyboardButton(text="📝 Пройти тестування")],
        [KeyboardButton(text="❓ Часті питання (FAQ)")],
        [KeyboardButton(text="📊 Мій прогрес")],
        [KeyboardButton(text="❗ Технічна підтримка")],
    ],
    resize_keyboard=True
)