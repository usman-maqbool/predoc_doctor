# Generated by Django 3.2.9 on 2022-10-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoinments', '0016_alter_qrcode_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/qr'),
        ),
    ]
