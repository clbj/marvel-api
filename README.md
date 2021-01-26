# CLBJ's Marvel's API GraphQl Version

This project provides a GraphQl API interface representing a simpler version of [Marvel's API](https://developer.marvel.com/).

It providers information about Marvel's Characters and Comics by searching for the character's name.

## Technical Stack

A set of distinct tools and libraries were used when developing this project, such as:
- Docker
- Kubernetes
- Python
- GraphQl
- JWT
- MongoDB

## Local Development Environment

VsCode was used as an editor when developing this project, but you can use any editor of your preference. Using VsCode will bring advantages since this project has a complete setup of VsCode's Remote Containers feature.

In **launch.json** you will find configurations for creating users, running the server, running tests, create migrations and migrate.

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

It is also important to set up your database. By default this project is using MongoDB, but you can replace it with any database of your choice. You can change the database configuration in the same **settings/common.py**.

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'marvelapi',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'marvel-api-db',
            'port': 27017
        },
    }
}
```

You can also choose different execution profiles by changing the **DJANGO_SETTINGS_MODULE** value in **manage.py** file. It is also possible to set this as an environment variable before executing the server.

## Accessing the API and Documentation

This a GraphQL API, so it uses a single URL for its resources. The default URL to access the API is **http://YOUR-HOST/api**. Since it is a self-documented API, you can use your browser to access a query interface and the resources documentation and schema specification.

The application uses JWT for access authorization, so it will be necessary to request access to a user previously created by running Django's create user command. For example, you can create an **admin** user by using the **Create Admin User** configuration available in the **launch.json** file or by running django's command as shown below.

```bash
python manage.py createsuperuser
```

The command will prompt asking for inputs.

### Generate a Token for Access

The API has secured resources that are only accessible by using a valid JWT. After creating a Django user, you will be able to request a JWT to be used for subsequent requests. You can do this by calling the tokenAuth service as described below:

```graphql
mutation {
  tokenAuth(username: "admin", password: "admin123"){
    token
  }
}
```

The service will respond with a valid JWT that can be used for subsequent service requests.

```json
{
  "data": {
    "tokenAuth": {
      "token": "3j5yd6XAiOiJKV1QiLCJhbGciJ9..."
    }
  }
}
```

When calling an application's resource, it is important to include the **Authorization: JWT <token>** to the header as the example below:

```bash
Authorization: "JWT 3j5yd6XAiOiJKV1QiLCJhbGciJ9..."
```

Example of an API call:

```graphql
query {
  characters(name: "Sider-man"){
    name
    description
  }
}
```

# Container Deployment

This project contains a Dockerfile and a Docker Compose file that enables the creation of a docker image. If you are using VsCode's Remote-containers for development, the image is already created in your local machine. You can also build the image by running the below command inside the project's **.devcontainer** folder.

```bash
docker-compose build
```

## Production Deployment

One suggestion of production deployment is using a container infrastructure supporting [Kubernetes](https://kubernetes.io/). In this project root folder you will find Yaml files with samples for a production deployment using Kubernetes to automate the deployment and scale the application. Remember to update Django's configuration with the allowed hosts as shown in the below example.

```python
ALLOWED_HOSTS = ['127.0.0.1', 'allowebhost.com']
```

## Future Improvements

There are a lot of opportunities to extend this project. It is possible to highlight these ones:
- Unit testing with mocked webservices.
- Usage of **concurrent.futures** library to execute parallel requests to Marvel's API.
- Add audit capabilities to monitor API calls.

## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

