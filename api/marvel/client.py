import requests
from dataclasses import dataclass
from django.conf import settings
from api.marvel.auth_generator import MarvelAuthGenerator

@dataclass
class MarvelClient():
    """
    A client class to connect to Marvel's API
    """


    def __get(self, query: dict) -> requests.Response:
        """
        Generic method to do GET calls using auth
        """
        auth = MarvelAuthGenerator.generate()

        headers = {
            'api-key': auth['api-key'],
            'ts': auth['ts'],
            'hash': auth['hash']
        }

        response = requests.get(
            settings.MARVEL['url'], 
            headers=headers, 
            params=query
        )

        return response