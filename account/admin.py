from django.contrib import admin
from .models import InvitedUser, UserModel

admin.site.register(UserModel)
admin.site.register(InvitedUser)