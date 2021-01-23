from django.contrib import admin
from api.models.User import User
from api.models.audit import Audit


admin.site.register(User)
admin.site.register(Audit)