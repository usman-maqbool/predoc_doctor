from django.contrib import admin
from .models import (
    InvitedDoctor,
    UserModel
)

admin.site.register(InvitedDoctor)
admin.site.register(UserModel)