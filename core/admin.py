import site
from django.contrib import admin
from .models import Appoinment, Patient ,DoctorObject, QuestionWare
# Register your models here.

admin.site.register(Patient)
admin.site.register(DoctorObject)
admin.site.register(Appoinment)
admin.site.register(QuestionWare)