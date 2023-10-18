import requests


url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20231018T053553Z.e6da0d47c013540a.2b34d3c6b0516cb2f9542ae357759f118d4d7654'


def translate_word(word):
    params = {'key': token,
              'lang': 'ru-en',
              'text': word,
              'ui': "ru"
              }

    response = requests.get(url=url, params=params).json()
    trans_word = response['def'][0]['tr'][0]['text']
    return trans_word


print(translate_word('Муж'))
