import requests

def build_query(
        keyword: list[str],
) -> str:
    """
        Формирует поисковый запрос из списка ключевых слов.

        :param keywords: Список ключевых слов.
        :return: Строка поискового запроса.
        """
    return ' '.join(keyword)

def fetch_vacancies(
        date:str,
        query: str,

) -> list[dict]:
    url = 'https://api.hh.ru/vacancies'

    headers = {
        "User-Agent": "lsn_hh_vacancies_parser/1.0 (github.com/Jd4rc))",
    }

    params = {
        'text': query,
        'per_page': 5,
    }

    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

    return data['items']


def parse_vacancies(
        data: dict,

) -> list[dict]:
    vacancies = []

    for item in data['items']:
        vacancies.append(
            {
                'name': item['name'],
                'company': item['employer']['name'],
                'url': item['alternative_url'],
            }
        )

    return vacancies
