import requests


def get_size(name):
    geocoder_api_server = 'http://geocode-maps.yandex.ru/1.x/'
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": name,
        "format": "json",
        'envelope': ''}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        pass
    json_response = response.json()
    low = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
        'lowerCorner'].split()
    up = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope'][
        'upperCorner'].split()
    low = [abs(float(elem)) for elem in low]
    up = [abs(float(elem)) for elem in up]
    return [str(abs(low[0] - up[0])), str(abs(low[1] - up[1]))]

