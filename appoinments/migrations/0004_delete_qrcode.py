# Generated by Django 3.2.9 on 2022-10-07 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appoinments', '0003_rename_username_qrcode_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QrCode',
        ),
    ]
