import datetime, hashlib
from dataclasses import dataclass
from django.conf import settings


@dataclass
class MarvelAuthGenerator():
    """
    Class to handle the Marvel's api hash generator
    """


    @staticmethod
    def generate() -> dict:
        """
        Generates the Marvel's API auth information

        :return: Dictionary with the auth params
        :rtype: dict
        """
        timestamp = datetime.datetime.now().timestamp()
        input_str = str(timestamp)+settings.MARVEL['private-key']+settings.MARVEL['public-key']

        return {
            'api-key': settings.MARVEL['public-key'],
            'ts': timestamp,
            'hash': hashlib.md5(input_str.encode()).hexdigest()
        }