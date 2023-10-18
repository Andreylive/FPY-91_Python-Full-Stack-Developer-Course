import requests


def get_the_smartest_superhero() -> str:
    my_heroes = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    all_heroes = requests.get(url).json()

    for hero in all_heroes:
        if hero['name'] in my_heroes:
            my_heroes[hero['name']] = hero['powerstats']['intelligence']
            sorted_herous = sorted(my_heroes.items(), key=lambda x: x[1], reverse=True)

    the_smartest_superhero = sorted_herous[0][0]
    return the_smartest_superhero

print(get_the_smartest_superhero())