import requests
import json



BASE_PATH = 'https://data.fixer.io/api/latest?access_key='


def get_rates(api_key):
    response = requests.get(BASE_PATH + api_key)
    if response.status_code == 200:
        return json.loads(response.text)
    return None