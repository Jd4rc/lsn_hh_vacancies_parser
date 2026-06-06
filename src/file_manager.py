import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def save_vacancies(
        vacancies: list[dict],
        filename: str
) -> None:
    file_path = BASE_DIR / 'data' / filename

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dumps(
            vacancies,
            file,
            ensure_ascii=False,
            indent=4,
        )