import requests


def get_the_smartest_superhero(heroes_id):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    all_heroes = requests.get(url).json()
    my_heroes = {}

    for hero in all_heroes:
        if hero['id'] in heroes_id:
            my_heroes[hero['name']] = hero['powerstats']['intelligence']

    sorted_heroes = sorted(my_heroes.items(), key=lambda x: x[1], reverse=True)
    the_smartest_superhero = sorted_heroes[0][0]

    return the_smartest_superhero


heroes_id = [1, 2, 3]
print(get_the_smartest_superhero(heroes_id))
