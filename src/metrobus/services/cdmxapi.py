import requests

from app.settings import MBAPI_URL


def get_data():
    json_data = None
    records = None

    r = requests.get(MBAPI_URL)

    if r.status_code == 200:
        json_data = r.json()

        if 'records' in json_data and len(json_data['records']) > 0:
            records = json_data['records']

    return records


