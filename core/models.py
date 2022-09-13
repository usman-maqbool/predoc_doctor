from django.db import models

# Create your models here.

class Doctor(models.Model):
    dr_name = models.CharField(max_length=150,blank=False,null=False)

class Patient(models.Model):
    name = models.CharField(max_length=150,blank=False,null=False)
    d_o_b = models.DateField(max_length=8)
    age = models.IntegerField(null=False, blank=False)
    last_check_doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='last_saw_by')
    recent_doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='last_see_dr')
    last_answere = models.DateTimeField()
