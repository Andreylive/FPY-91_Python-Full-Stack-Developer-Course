import requests

url = 'https://geocode.maps.co/reverse'
city_list = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']


def find_uk_city(coordinates: list) -> str:
    "Find a city with coordinates using geocode api"
    for lat, lon in coordinates:
        params = {'lat': lat, 'lon': lon}
        response = requests.get(url=url, params=params).json()['address']['city']
        if response in city_list:
            city = response
    return city


coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]

print(find_uk_city(coordinates))
