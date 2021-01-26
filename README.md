# CLBJ's Marvel's API GraphQl Version

This project provides a GraphQl API interface representing a simpler version of [Marvel's API](https://developer.marvel.com/).

It providers information about Marvel's Characters and Comics by searching for the character's name.

## Technical Stack

Different set of tools were used when developing this project, such as:
- Docker
- Kubernetes
- Python
- GraphQl
- JWT

## Local Development Environment

VsCode was used as editor when developing this project, but you can use any editor of your preference. Using VsCode will bring  advantages since this project has a complete setup of VsCode's Remote Containers feature.

In **launch.json** you will find configurations for runnning the server, running tests, create migrations and migrate.

## Configuring the API

To access Marvel's developer API it is necessary to request an API key. You can follow the instructions at Marvel's website to request one. With your key in hand, it will be necessary to update the configuration file located in the **settings/common.py** file. Replace the values for **private-key** and **public-key** with the ones obtained.


```python
MARVEL = {
    'url': 'https://gateway.marvel.com/v1/public/',
    'private-key': 'YOUR-PRIVATE-KEY-HERE',
    'public-key': 'YOUR-PUBLIC-KEY-HERE',
    'limit': 100
}
```

You can also choose different execution profiles by changing the **DJANGO_SETTINGS_MODULE** value in **manage.py** file. It is also possible to set this as a environment variable before executing the server.





## License
[MIT](https://choosealicense.com/licenses/mit/)

