# Generated by Django 3.2.9 on 2022-10-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_inviteduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inviteduser',
            name='is_agree',
        ),
        migrations.AddField(
            model_name='inviteduser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
