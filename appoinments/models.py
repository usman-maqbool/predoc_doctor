
from django.db import models
from account.models import UserModel
import random
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
class Questionire(models.Model):
    syptoms = models.JSONField(default= dict)

class Appoinment(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    patient = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='patient')
    doctor = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='doctor')
    qs = models.OneToOneField(Questionire,on_delete=models.CASCADE,null=True,blank=True)


class QrCode(models.Model):

   # url=models.URLField()
    user = models.OneToOneField(UserModel,on_delete=models.CASCADE, blank=True, null=True) 
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    image=models.ImageField(upload_to='qrcode',blank=True)

   

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.first_name)
        sec_img=qrcode.make(self.last_name)
        canvas=Image.new("RGB", (300,300),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        canvas.paste(sec_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)