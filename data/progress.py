import json
import os
from typing import Dict
import logging
from data.shared import courses

# Абсолютний шлях до файлу з прогресом
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "user_progress.json")

user_progress: Dict[int, Dict] = {}

# Завантаження прогресу з файлу
def load_progress():
    global user_progress
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            user_progress = json.load(f)
            # Ключі з JSON завжди строки — потрібно перетворити в int
            user_progress = {int(k): v for k, v in user_progress.items()}
            logging.info("User progress loaded.")
    else:
        user_progress = {}

# Збереження прогресу у файл
def save_progress():
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(user_progress, f, ensure_ascii=False, indent=2)
        logging.info("User progress saved.")

# Ініціалізація прогресу для нового користувача
def initialize_user_progress(user_id: int):
    if user_id not in user_progress:
        user_progress[user_id] = {"courses": {}}

    for course_id, course_data in courses.items():
        course_progress = user_progress[user_id]["courses"].setdefault(course_id, {"modules": {}, "total_modules": 0})
        course_progress["total_modules"] = len(course_data["modules"])
    save_progress()

# Оновлення прогресу модуля (відмітка як завершеного)
def update_module_progress(user_id: int, course_id: str, module_id: str):
    logging.info(f"Updating module progress: user_id={user_id}, course_id={course_id}, module_id={module_id}")
    initialize_user_progress(user_id)
    course_progress = user_progress[user_id]["courses"].setdefault(course_id, {"modules": {}, "total_modules": 0})
    module_progress = course_progress["modules"].setdefault(module_id, {"completed": False, "test_score": 0.0})
    module_progress["completed"] = True
    save_progress()

# Оновлення результату тесту для модуля
def update_test_score(user_id: int, course_id: str, module_id: str, score: float):
    logging.info(f"Updating test score: user_id={user_id}, course_id={course_id}, module_id={module_id}, score={score}")
    initialize_user_progress(user_id)
    course_progress = user_progress[user_id]["courses"].setdefault(course_id, {"modules": {}, "total_modules": 0})
    module_progress = course_progress["modules"].setdefault(module_id, {"completed": False, "test_score": 0.0})
    module_progress["test_score"] = score
    save_progress()

# Отримати прогрес користувача (повертає словник)
def get_user_progress(user_id: int):
    initialize_user_progress(user_id)
    return user_progress[user_id]
