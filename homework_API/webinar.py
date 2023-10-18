import requests
import json
from pprint import pprint

# 1. https://gorest.co.in/

base_url = 'https://gorest.co.in/'

# список пользователей
# response = requests.get(base_url + '/public/v2/users')
# if 200 <= response.status_code < 300:
#     pprint(response.json())


# список пользователей c параметрами

# params_dict = {
#     'page': 4,
#     'per_page': 3
# }
# response = requests.get(base_url + '/public/v2/users', params=params_dict)
# if 200 <= response.status_code < 300:
#     pprint(response.json())


# создать пользователя

# payload = {
#     "name": "Тим",
#     "email": "dfhdfhd1fhd2fh@howesll-parker.example",
#     "gender": "male",
#     "status": "active"
# }
# headers_dict = {
#     'Authorization': 'Bearer 33c71a348b315e9a3315a497513f2505c06da081459efe4842643c2abebe4cb4',
#     'Content-Type': "application/json",
#     'User-Agent': 'My-agent'
# }
# # response = requests.post(base_url + '/public/v2/users',
# #                          json=payload,
# #                          headers=headers_dict)
# response = requests.post(base_url + '/public/v2/users',
#                          data=json.dumps(payload),
#                          headers=headers_dict)
# print(response.json())
# print(response.request.headers)


# 2. работа с файлами и яндекс диском
#
# response = requests.get('https://rgo.ru/upload/s34web.imageadapter/3391b95c081666cc16ceb5b195d7ccf4/oleg_bogdanov_amurskiy_tigr_592345.jpg')
# with open('Тигр.jpg', 'wb') as file:
#     file.write(response.content)
#
# # работа c яндекс диском
#
# token = 'OAuth y0_AgAAAABnENF7AADLWwAAAADW0Zr0rLgkxmptRpqgS1mkh6kZ5279rAg'
# headers = {
#     'Authorization': token
# }
#
# # создание папки на ЯД
# params = {'path': 'Image'}
# response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
#                         params=params,
#                         headers=headers)
# print(response.json())
#
# # Запрос адреса загрузки
# params = {'path': 'Image/tiger.jpg'}
# response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
#                         params=params,
#                         headers=headers)
# url_for_upload = response.json().get('href')
#
# # загрузка файла
# with open('Тигр.jpg', 'rb') as file:
#     response = requests.put(url_for_upload, files={"file": file})
#     print(response)


# my_heroes = {
#     'Hulk': 0,
#     'Captain America': 0,
#     'Thanos': 0
# }
#
# url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
#
# all_heroes = requests.get(url).json()
# for hero in all_heroes:
#     # print(hero.get('name'), hero.get('powerstats', {}).get('durability')) # первый вариант
#     if hero['name'] in my_heroes: # второй вариант
#         my_heroes[hero['name']] = hero['powerstats']['speed']
#
# print(my_heroes)

