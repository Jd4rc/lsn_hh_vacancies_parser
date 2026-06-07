import json
from pathlib import Path
from src.logger import logger

BASE_DIR = Path(__file__).resolve().parent.parent

def save_vacancies(
        vacancies: list[dict],
        filename: str
) -> None:
    """
       Сохраняет список вакансий в JSON-файл в директории data.

       :param vacancies: Список словарей с данными о вакансиях.
       :param filename: Имя JSON-файла.
       :return: None.
       """
    file_path = BASE_DIR / 'data' / filename

    logger.info('Saving vacancies to file', file_path)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dumps(
            vacancies,
            file,
            ensure_ascii=False,
            indent=4,
        )

    logger.info('Successfully saved %s vacancies', len(vacancies))

def build_filename(
        date:str,
        keywords: list[str],
) -> str:
    """
        Формирует имя JSON-файла на основе даты и ключевых слов.

        :param date: Дата поиска вакансий.
        :param keywords: Список ключевых слов запроса.
        :return: Имя файла в формате YYYY-MM-DD_keyword1_keyword2.json.
        """
    query_part = '_'.join(keywords)

    return f'{date}_{query_part}.json'
