import requests

from app.settings import MBAPI_URL


def get_data():
    """ Get response from CDMX API from metrobus location points and return a dict
    https://datos.cdmx.gob.mx/explore/dataset/prueba_fetchdata_metrobus/api/?rows=5
    """
    json_data = None
    records = None

    r = requests.get(MBAPI_URL)

    if r.status_code == 200:
        json_data = r.json()

        if 'records' in json_data and len(json_data['records']) > 0:
            records = json_data['records']

    return records


