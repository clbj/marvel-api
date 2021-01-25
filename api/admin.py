from django.contrib import admin
from api.models.user import User
from api.models.audit import Audit


admin.site.register(User)
admin.site.register(Audit)