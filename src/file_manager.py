import json
from pathlib import Path

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

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dumps(
            vacancies,
            file,
            ensure_ascii=False,
            indent=4,
        )

def build_filename(
        date:str,
        keywords: list[str],
) -> str:
    query_part = '_'.join(keywords)

    return f'{date}_{query_part}.json'
