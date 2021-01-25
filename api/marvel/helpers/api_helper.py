from dataclasses import dataclass

@dataclass
class MarvelApiHelper():

    @staticmethod
    def filter_characters_response(data: dict) -> dict:
        """
        Helper method to assist on filtering Marvel's API
        characters to a simple one

        :param data: Dictionary with the inputs of the API
        :type data: dict
        :return: A dictionary with the results
        :rtype: dict
        """
        output = {
            'code': data['code'],
            'status': data['status'],
            'etag': data['etag'],
            'offset': data['data']['offset'],
            'total': data['data']['total'],
            'count': data['data']['count']
        }

        output['characters'] = list()

        for i in range(data['data']['total']):
            character = {
                'id': data['data']['results'][i]['id'],
                'name': data['data']['results'][i]['name'],
                'description': data['data']['results'][i]['description'],
                'modified': data['data']['results'][i]['modified']
            }
            output['characters'].append(character)

        del(data)
        return output


    @staticmethod
    def filter_comics_response(data:dict) -> dict:
        """
        Helper method to assist on filtering Marvel's API
        comics to a simple one

        :param data: Dictionary with the inputs of the API
        :type data: dict
        :return: A dictionary with the results
        :rtype: dict
        """
        output = {
            'code': data['code'],
            'status': data['status'],
            'etag': data['etag'],
            'offset': data['data']['offset'],
            'total': data['data']['total'],
            'count': data['data']['count']
        }

        output['comics'] = list()

        for entry in data['data']['results']:
            comic = {
                'id': entry['id'],
                'digitalId': entry['digitalId'],
                'title': entry['title'],
                'issueNumber': entry['issueNumber'],
                'issn': entry['issn'],
                'pageCount': entry['pageCount'],
                'format': entry['format'],
                'modified': entry['modified']
            }
            output['comics'].append(comic)

        del(data)
        return output


    @staticmethod
    def remove_duplicated_results(first: list, second: list) -> dict:
        """
        Helper method to remove ducplicates form a Marvel's API request

        :param first: List with the results of one request
        :type first: dict
        :param second: List with the results of a second request
        :type second: dict
        :return: A dictionary with the results
        :rtype: dict
        """
        output = list()
        visited = set()

        for entry in first:
            visited.add(entry['id'])
            result = {
                entry['id']: entry
            }
            output.append(result)
        
        for entry in second:
            if entry['id'] not in visited:
                visited.add(entry['id'])
                result = {
                    entry['id']: entry
                }
                output.append(result)

        del(visited)
        return output