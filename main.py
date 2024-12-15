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

def ensure_output_directory():
    """Создает директорию для вывода, если ее нет."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        logger.info(f"Создана директория: {OUTPUT_DIR}")

def fetch_data_from_api(url: str) -> List[Dict]:
    """Загружает данные с API."""
    logger.info(f"Запрос данных с {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logger.info("Данные успешно получены.")
        return response.json()
    else:
        logger.error(f"Ошибка при запросе API: {response.status_code}")
        return []
    
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

def save_data_to_file(data: List[Dict], filename: str):
    """Сохраняет данные в файл."""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
        logger.info(f"Данные сохранены в файл {filepath}.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"Произошла ошибка: {e}")
