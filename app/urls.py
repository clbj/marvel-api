from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from ariadne.contrib.django.views import GraphQLView
from api.graphql import resolvers


urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/', GraphQLView.as_view(schema=resolvers.schema)),
]