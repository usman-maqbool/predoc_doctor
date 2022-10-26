
from account.models import UserModel
from django.db import models


class Questionire(models.Model):
    syptoms = models.JSONField(default= dict)

class Appoinment(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    patient = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='patient')
    doctor = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='doctor')
    qs = models.OneToOneField(Questionire,on_delete=models.CASCADE,null=True,blank=True)



import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random
import time




class QrCode(models.Model):
    # name=models.CharField(max_length = 255, blank = True)
    url=models.URLField()
    image=models.ImageField(upload_to='media/qr', blank=True)

    def save(self,*args,**kwargs):
        # qrcode_img=qrcode.make(self.url)
        # canvas=Image.new("RGB", (300,300),"white")
        # draw=ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # buffer=BytesIO()
        # canvas.save(buffer,"PNG")
        # self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        # canvas.close()
        # super().save(*args,**kwargs)


        qrcode_img=qrcode.make(self.url)
        canvas=Image.new("RGB", (290,290), "white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        # files_name = f'{self.url}-{self.id}qr.png'
        fname = f'image-{self.url}.png'
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        # self.image.save(f'image{random.randint(0,9999)}.png' ,File(buffer), save=False)
        self.image.save(f'{self.url}-{self.id}qr.png' ,File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)


    # def save(self,*args,**kwargs):
        
        # data = qrcode.make(self.url)
        # img = make(data)
        # buffer=BytesIO()
        # self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        # img.save(self.image)


        
        # qrcode_img=qrcode.make(self.url)
        # canvas=Image.new("RGB", (300,300),"white")
        # draw=ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # buffer=BytesIO()
        # canvas.save(buffer,"PNG")
        # self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        # canvas.close()
        # super().save(*args,**kwargs)

        
        
        # qrcode_img=qrcode.make(self.name)
        # canvas=Image.new("RGB", (290,290), "white")
        # draw=ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # # files_name = f'{self.url}-{self.id}qr.png'
        # fname = f'image-{self.name}.png'
        # buffer=BytesIO()
        # canvas.save(buffer,"PNG")
        # # self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        # self.image.save(fname, File(buffer), save=False)
        # canvas.close()
        # super().save(*args,**kwargs)


