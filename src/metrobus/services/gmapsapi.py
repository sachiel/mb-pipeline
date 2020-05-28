import requests

from app.settings import GOOGLE_APIKEY


def get_address(lat, lon, text=False):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}".format(
        lat,
        lon,
        GOOGLE_APIKEY
    )
    r = requests.get(url)

    if r.status_code == 200:
        if text:
            return r.text

        return r.json()

    return None


def process_address(data):
    address = {
        'address': '',
        'county': '',
        'zipcode': '',
        'city': ''
    }

    if data['status'] != 'OK':
        return address

    if 'results' in data and data['results']:
        for res in data['results']:
            if 'street_address' in res['types'] and not address['address']:
                address['address'] = res['formatted_address']

                for comp in res['address_components']:
                    if 'sublocality_level_1' in comp['types']:
                        address['county'] = comp['long_name']

                    if 'postal_code' in comp['types']:
                        address['zipcode'] = comp['long_name']

            if 'administrative_area_level_3' in res['types'] and not address['city']:
                for comp in res['address_components']:
                    if 'administrative_area_level_3' in comp['types']:
                        address['city'] = comp['long_name']

    return address

