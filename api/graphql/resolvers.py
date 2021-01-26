from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType
from ariadne_jwt import resolve_verify, resolve_refresh, resolve_token_auth, jwt_schema, GenericScalar
from ariadne_jwt.decorators import login_required
from api.models.user import User
from api.models.audit import Audit
from api.marvel.client import MarvelClient


type_defs = [
    load_schema_from_path("api/graphql/schema.graphql"),
    load_schema_from_path("api/graphql/jwt.graphql")
]

query = QueryType()
mutation = MutationType()

mutation.set_field('verifyToken', resolve_verify)
mutation.set_field('refreshToken', resolve_refresh)
mutation.set_field('tokenAuth', resolve_token_auth)

@query.field('characters')
@login_required
def resolve_characters(_, info, name):
    client = MarvelClient()
    result = client.get_characters(name=name)
    return result['characters']


@query.field('comics')
@login_required
def resolve_comics(_, info, name, limit=None):
    client = MarvelClient()
    result = client.get_comics(name=name, limit=limit)

    return result['comics']


@query.field('getAll')
@login_required
def resolve_all(_, info, name, limit=None):
    client = MarvelClient()
    result_characters = client.get_characters(name=name)
    result_comics = client.get_comics(name=name, limit=limit)

    return {
        'characters': result_characters['characters'],
        'comics': result_comics['comics']
    }

schema = make_executable_schema(type_defs,query,mutation,GenericScalar)