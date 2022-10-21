
from django.db import models
from account.models import UserModel

class Questionire(models.Model):
    syptoms = models.JSONField(default= dict)

class Appoinment(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    patient = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='patient')
    doctor = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='doctor')
    qs = models.OneToOneField(Questionire,on_delete=models.CASCADE,null=True,blank=True)

class QrCode(models.Model):
    url=models.URLField(blank=True)
    image=models.ImageField(upload_to='media',blank=True)
