from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType
from ariadne_jwt import resolve_verify, resolve_refresh, resolve_token_auth, jwt_schema, GenericScalar
from api.models.user import User
from api.models.audit import Audit


type_defs = [
    load_schema_from_path("api/graphql/schema.graphql"),
    load_schema_from_path("api/graphql/characters.graphql"),
    load_schema_from_path("api/graphql/comics.graphql")
]

query = QueryType()
mutation = MutationType()


@query.field('users')
def resolve_users(*_):
    return User.objects.all()


@query.field('audit')
def resolve_users(*_):
    return Audit.objects.all()


schema = make_executable_schema(type_defs, query, mutation)