# Generated by Django 3.2.9 on 2022-10-26 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appoinments', '0017_alter_qrcode_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrcode',
            old_name='name',
            new_name='url',
        ),
    ]