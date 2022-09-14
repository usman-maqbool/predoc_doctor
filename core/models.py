
from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta
import jsonfield
class DoctorObject(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female"),
)

class QuestionWare(models.Model):
    syptoms = models.JSONField(default= dict)
class Patient(models.Model):
    patient_first_name = models.CharField(max_length=150)
    patient_last_name = models.CharField(max_length=150)
    d_o_b = models.DateField(max_length=8)
    # last_check_doctor =  models.ForeignKey(DoctorObject,on_delete=models.CASCADE,related_name='last_saw_by')
    # recent_doctor = models.ForeignKey(DoctorObject,on_delete=models.CASCADE,related_name='last_see_dr')
    last_answere = models.DateTimeField()
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = 'male')
    details = models.ForeignKey(QuestionWare,on_delete=models.CASCADE)
    def __str__(self):
        return self.patient_first_name

    @property
    def Age(self):
        today = date.today()
        tottal_age = self.d_o_b - today
        # rdelta = relativedelta(today, tottal_age)
        total_age_stripped = str(tottal_age).split(",", 1)[0]
        return total_age_stripped
    


class Appoinment(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorObject,on_delete=models.CASCADE )