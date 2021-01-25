import requests, json, logging
from dataclasses import dataclass, field
from django.conf import settings
from api.marvel.auth_generator import MarvelAuthGenerator
from api.marvel.helpers.api_helper import MarvelApiHelper

@dataclass
class MarvelClient():
    """
    A client class to connect to Marvel's API
    """
    session: requests.Session() = field(default_factory=requests.session)


    def __post_init__(self):
        """
        Post init method to start common requests arguments
        """
        auth = MarvelAuthGenerator.generate()

        params = {
            'apikey': auth['apikey'],
            'ts': auth['ts'],
            'hash': auth['hash']
        }

        self.session.params = params


    def __get(self, query: dict, url=None) -> requests.Response:
        """
        Generic method to do GET calls using auth
        """
        try:
            if url is not None:
                url = settings.MARVEL['url'] + str(url)

            query.update(self.session.params)
        except ConnectionError:
            print(f"MarvelClient: ConnectionError")
        except Exception as e:
            print(f"MarvelClient: {e}")
        
        return self.session.get(url, params=query)


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

    
    def get_comics(self, name: str, limit: int=None) -> dict:
        """
        Execute a request to Marvel's api and collect the
        comics information of a character

        :param name: Name of the character
        :type name: str
        :return: A dictionary with the results
        :rtype: dict
        """
        executions = 1
        query = {
            'title': name,
            'limit': int(settings.MARVEL['limit']),
            'offset': 0
        }

        number_records = int(settings.MARVEL['limit'])
        if limit is not None and limit < int(settings.MARVEL['limit']):
            number_records = limit
            query['limit'] = limit

        response = self.__get(query, 'comics')
        result = json.loads(response.text)
        result = MarvelApiHelper.filter_comics_response(result)

        if limit is not None:
            if limit > int(settings.MARVEL['limit']) and limit < result['total']:
                number_records = limit
            elif limit >= result['total']:
                number_records = result['total']           

        if number_records > int(settings.MARVEL['limit']):
            executions = int(float(number_records/100))
            query['offset'] = int(settings.MARVEL['limit'])+1

            while executions > 0:
                response = self.__get(query, 'comics')
                result_execution = json.loads(response.text)
                result_execution = MarvelApiHelper.filter_comics_response(result_execution)
                # updating the result list
                result['comics'].extend(result_execution['comics'])
                executions = executions-1
                query['offset'] = query['offset'] + int(settings.MARVEL['limit'])

        return result