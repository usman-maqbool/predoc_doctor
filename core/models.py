
from django.db import models


class Appoinment(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorObject,on_delete=models.CASCADE )
    qs    = # add a 101 relation to qs



class QuestionWare(models.Model):
    syptoms = models.JSONField(default= dict) 