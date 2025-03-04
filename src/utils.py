import os
import pandas as pd
from src.my_logging import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "utils.log")
logger = get_logger("utils", file_path)

def open_file(filepath: str = '') -> list:
    """
    Функция принимает на вход путь к файлу находящегося в директории Data, определяет какой формат файла
    и в зависимости от формата файла выбирает обработку файла
    :param filepath:
    :return:
    """



    try:
        basename, extension = os.path.splitext(filepath)  # Определяем расширение файла оно будет записано в 'extension'

        logger.info(f'Чтение файла {filepath}')

        data = []

        if extension == '.xlsx':  # Если файл Excel
            data = pd.read_excel(filepath).to_dict("records")
        elif extension == '.csv':
            data = pd.read_csv(filepath, sep=";").to_dict("records")  # 'sep' это выбор разделителя

        logger.info(f'Возвращает список из 5 операций: {data[0:5]}')
        return data

    except FileNotFoundError:

        raise FileNotFoundError('Файл не найден')
