import json
import os

from src.my_logging import get_logger
from datetime import datetime


# json - V, # requests - , # API - , # datetime - V, # logging - V, # pytest - , # pandas - V



current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "views.log")
logger = get_logger("views", file_path)


def return_json_answer(data_hour_str: str) -> str:
    """
    Функция принимает на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS,
    возвращает словарь с приветствием
    :return:
    """
    hour = int(data_hour_str.split(" ")[1].split(":")[0])  # Извлекаем часы
    logger.info(f'Получено значение часов: {hour}')
    if 6 <= hour < 12:
        greetings_hour = "Доброе утро"
    elif 12 <= hour < 18:
        greetings_hour = "Добрый день"
    elif 18 <= hour < 24:
        greetings_hour = "Добрый вечер"
    else:
        greetings_hour = "Доброй ночи"

    logger.info(f'Пользователь получил приветствие: {greetings_hour}')
    return greetings_hour


def date_operations_filtering(data_str: str) -> str:
    """
    Функция на вход получает строку с датой, преобразовывает её в datetime объект, создает дату начала месяца.
    Возвращает строку диапазона дат формата "dd.mm.YYYY-dd.mm.YYYY"
    :param data_str:
    :return:
    """

    date_obj = datetime.strptime(data_str, "%d.%m.%Y")  # Создаем объект datetime, для изменения данных
    logger.info(f'Преобразовываем из строки в объект datetime: {date_obj}')

    start_of_month = date_obj.replace(day = 1).strftime("%d.%m.%Y")  # Создаем дату начала месяца и возвращаем строку
    logger.info(f'Создаем дату начала месяца и возвращаем в строку: {start_of_month}')

    date_range = start_of_month + '-' + data_str  # Возвращает строку диапазона дат формата "dd.mm.YYYY-dd.mm.YYYY"

    logger.info(f'Возвращаем строку диапазона дат: {date_range}')
    return date_range


default_settings = {
    "greeting": return_json_answer('2023-10-05 14:30:00'),
    "cards": [],
    "top_transactions": [],
    "currency_rates": [],
    "stock_prices": []
}


with open("user_settings.json", "w", encoding = "UTF-8") as file:  # Открывание файла для записи
    json.dump(default_settings, file, ensure_ascii=False, indent=4)  # Записываем дефолтный шаблон




settings = {
    "greeting": "Добрый день",
    "cards": [
        {"last_digits": "5814", "total_spent": 1262.00, "cashback": 12.62},
    ],
    "top_transactions": [
        {
            "date": "21.12.2021",
            "amount": 1198.23,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
    ],
    "currency_rates": [
        {"currency": "USD", "rate": 73.21},
        {"currency": "EUR", "rate": 87.08},
    ],
    "stock_prices": [
        {"stock": "AAPL", "price": 150.12},
        {"stock": "AMZN", "price": 3173.18},
    ],
}
