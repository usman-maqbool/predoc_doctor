# Generated by Django 3.2.9 on 2022-10-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoinments', '0018_rename_name_qrcode_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qrcode',
            options={'verbose_name': 'Qr Code'},
        ),
        migrations.RenameField(
            model_name='appoinment',
            old_name='date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='appoinment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appoinment',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='appoinment',
            name='qs',
        ),
        migrations.AddField(
            model_name='appoinment',
            name='questions',
            field=models.JSONField(default=dict),
        ),
        migrations.DeleteModel(
            name='Questionire',
        ),
    ]