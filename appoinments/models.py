import random
from io import BytesIO

import qrcode
from account.models import UserModel
from django.core.files import File
from django.db import models
from PIL import Image, ImageDraw


class Questionire(models.Model):
    syptoms = models.JSONField(default= dict)

class Appoinment(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    doctor = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='doctor')
    qs = models.OneToOneField(Questionire,on_delete=models.CASCADE,null=True,blank=True)

class QrCode(models.Model):
    class Meta:
        verbose_name = 'Qr Code'
    url=models.URLField()
    image=models.ImageField(upload_to='media/qr', blank=True)

    def save(self,*args,**kwargs):
        url = self.url
        qrcode_img=qrcode.make(url)
        canvas=Image.new("RGB", (400,400), "white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}.png' ,File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)


