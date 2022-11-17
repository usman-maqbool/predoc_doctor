import random
from io import BytesIO

import qrcode
from account.models import UserModel
from django.core.files import File
from django.db import models
from PIL import Image, ImageDraw
from .parser import Parser

class Appoinment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    questions = models.JSONField(default= dict)
    age = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.CharField(max_length=255, null=True, blank=True)


    def save(self, *args, **kwargs):
        parser = Parser(self.questions)
        self.name = parser.get_first_name()
        self.date_of_birth = parser.get_date_of_birth()
        self.age = parser.get_age()
        return super().save(*args, **kwargs)



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


