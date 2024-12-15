# Импортируем необходимые модули
import os
import sys
import random
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Константы
DATA_DIR = "data"
LOGS_DIR = "logs"
CONFIG_FILE = "config.json"

# Утилиты

def ensure_directories_exist():
    """Создает необходимые директории, если их нет."""
    for directory in [DATA_DIR, LOGS_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"Создана директория: {directory}")

def load_config() -> Dict[str, Any]:
    """Загружает конфигурацию из JSON файла."""
    if not os.path.exists(CONFIG_FILE):
        logger.warning(f"Конфигурационный файл {CONFIG_FILE} не найден. Используются настройки по умолчанию.")
        return {}
    with open(CONFIG_FILE, 'r') as file:
        config = json.load(file)
        logger.info("Конфигурация успешно загружена.")
        return config

def save_config(config: Dict[str, Any]):
    """Сохраняет конфигурацию в JSON файл."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)
        logger.info("Конфигурация успешно сохранена.")

# Основные функции

def generate_random_data(size: int) -> List[int]:
    """Генерирует список случайных чисел."""
    logger.info(f"Генерация {size} случайных чисел.")
    return [random.randint(0, 100) for _ in range(size)]

def save_data_to_file(data: List[int], filename: str):
    """Сохраняет данные в файл."""
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file)
        logger.info(f"Данные сохранены в файл {filepath}.")

def load_data_from_file(filename: str) -> List[int]:
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        logger.error(f"Файл {filepath} не найден.")
        return []
    with open(filepath, 'r') as file:
        data = json.load(file)
        logger.info(f"Данные загружены из файла {filepath}.")
        return data

# Пример работы с данными

def analyze_data(data: List[int]):
    """Анализирует данные и выводит статистику."""
    if not data:
        logger.warning("Нет данных для анализа.")
        return
    logger.info(f"Количество элементов: {len(data)}")
    logger.info(f"Минимальное значение: {min(data)}")
    logger.info(f"Максимальное значение: {max(data)}")
    logger.info(f"Среднее значение: {sum(data) / len(data):.2f}")

# Основная программа

def main():
    ensure_directories_exist()
    config = load_config()

    # Установка значения по умолчанию
    data_size = config.get("data_size", 10)
    output_file = config.get("output_file", "output.json")

    # Генерация данных
    data = generate_random_data(data_size)

    # Сохранение данных
    save_data_to_file(data, output_file)

    # Загрузка данных и их анализ
    loaded_data = load_data_from_file(output_file)
    analyze_data(loaded_data)

    # Обновление конфигурации
    config["last_run"] = datetime.now().isoformat()
    save_config(config)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"Произошла ошибка: {e}")
