from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType
from ariadne_jwt import resolve_verify, resolve_refresh, resolve_token_auth, jwt_schema, GenericScalar
from ariadne_jwt.decorators import login_required
from api.models.user import User
from api.models.audit import Audit


type_defs = [
    load_schema_from_path("api/graphql/schema.graphql"),
    load_schema_from_path("api/graphql/jwt.graphql"),
    load_schema_from_path("api/graphql/characters.graphql"),
    #load_schema_from_path("api/graphql/comics.graphql")
]

query = QueryType()
mutation = MutationType()

mutation.set_field('verifyToken', resolve_verify)
mutation.set_field('refreshToken', resolve_refresh)
mutation.set_field('tokenAuth', resolve_token_auth)



schema = make_executable_schema(type_defs,query,mutation,GenericScalar)