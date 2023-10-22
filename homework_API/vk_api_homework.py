from urllib.parse import urlencode
import requests
from pprint import pprint

APP_ID = '51774886'
OAUTH_BASE_URL = 'https://oauth.vk.com/authorize'

params = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'page',
    'scope': 'status,photos',
    'response_type': 'token'
    }

oauth_url = f"{OAUTH_BASE_URL}?{urlencode(params)}"
print(oauth_url)

token = 'my_token'

class VKAPIClient:

    API_BASE_URL = 'https://api.vk.com/method'

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
                'access_token': self.token,
                'v': '5.131'
        }

    def _build_url(self, api_method):
        return f'{self.API_BASE_URL}/{api_method}'

    def get_status(self):
        params = self.get_common_params()
        params.update({'user_id': self.user_id})
        response = requests.get(self._build_url('status.get'), params=params)
        return response.json().get('response', {}).get('text')

    def set_status(self, new_status):
        params = self.get_common_params()
        params.update({'user_id': self.user_id, 'text': new_status})
        response = requests.get(self._build_url('status.set'), params=params)
        response.raise_for_status()

    def replace_status(self, target, replace_string):
        status = self.get_status()
        new_status = status.replace(target, replace_string)
        self.set_status(new_status)

    def get_profile_photos(self):
        params = self.get_common_params()
        params.update({'owner_id': self.user_id, 'album_id': 'profile'})
        response = requests.get(self._build_url('photos.get'), params=params)
        return response.json()


if __name__ == '__main__':
    vk_client = VKAPIClient(token, 1396185)
    pprint(vk_client.get_status())
    vk_client.replace_status('Статус', 'Новый статус')
    photos_info = vk_client.get_profile_photos()
    pprint(photos_info)
