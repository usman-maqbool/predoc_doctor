from django.contrib import admin
from .models import Appoinment, QrCode

admin.site.register(Appoinment)
# admin.site.register(Questionire)      
admin.site.register(QrCode)
