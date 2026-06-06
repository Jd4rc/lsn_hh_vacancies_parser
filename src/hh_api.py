import requests

def fetch_vacancies(
        date:str,
        query: str,

) -> list[dict]:
    url = 'https://api.hh.ru/vacancies'

    params = {
        'text': query,
        'date_from': date,
        'date_to':date,
        'per_page': 50,
        'page':0
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()['items']