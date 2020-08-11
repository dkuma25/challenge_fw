import requests
from django.apps import AppConfig


class ApiSyncConfig(AppConfig):
    name = 'api_sync'

    # def ready(self):
    #     API_URL = 'https://jsonplaceholder.typicode.com'
    #     try:
    #         url = '{}/albums'.format(API_URL)
    #         response = requests.get(url)
    #         json = response.json()
    #         print(json)
    #     except Exception as e:
    #         print(e)
