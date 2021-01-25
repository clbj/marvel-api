from .common import *

DEBUG = True

MARVEL = {
    'url': 'https://gateway.marvel.com/v1/public/',
    'private-key': 'YOUR-PRIVATE-KEY-HERE',
    'public-key': 'YOUR-PUBLIC-KEY-HERE',
    'limit': 100
}

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'marvelapi',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'marvel-api-db',
            'port': 27017
        },
    },
    'LOGGING': {
        'version': 1,
        'loggers': {
            'djongo': {
                'level': 'DEBUG',
                'propagate': False,                        
            }
        }
    }
}