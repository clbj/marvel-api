import requests, json
from dataclasses import dataclass
from django.conf import settings
from api.marvel.auth_generator import MarvelAuthGenerator
from api.marvel.helpers.api_helper import MarvelApiHelper

@dataclass
class MarvelClient():
    """
    A client class to connect to Marvel's API
    """

    def __get(self, query: dict, url=None) -> requests.Response:
        """
        Generic method to do GET calls using auth
        """
        if url is not None:
            url = settings.MARVEL['url'] + str(url)

        auth = MarvelAuthGenerator.generate()

        params = {
            'apikey': auth['apikey'],
            'ts': auth['ts'],
            'hash': auth['hash']
        }
        query.update(params)

        response = requests.get(
            url,  
            params=query
        )

        return response


    def get_characters(self, name: str) -> dict:
        """
        Execute a request to Marvel's api and collect a
        character information

        :param name: Name of the character
        :type name: str
        :return: A dictionary with the results
        :rtype: dict
        """
        query = {'name': name}
        response = self.__get(query, 'characters')
        result = json.loads(response.text)
        return MarvelApiHelper.filter_characters_response(result)

    
    def get_comics(self, name: str, limit=settings['MARVEL']['limit']) -> dict:
        """
        Execute a request to Marvel's api and collect the
        comics information of a character

        :param name: Name of the character
        :type name: str
        :return: A dictionary with the results
        :rtype: dict
        """

        # get the character id
        characters = self.get_characters(name)
        query = {'title': name, 'limit': limit}

        for i in range(len(characters['characters'])):
            if i == 0:
                query['characters'] = str(characters['characters'][i]['id'])
            else:
                query['characters'] = query['characters'] + "," + str(characters['characters'][i]['id'])

        response = self.__get(query, 'comics')
        result = json.loads(response.text)
        return MarvelApiHelper.filter_comics_response(result)