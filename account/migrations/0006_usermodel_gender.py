# Generated by Django 3.2.9 on 2022-09-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20220915_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='gender',
            field=models.IntegerField(blank=True, choices=[('male', 'male'), ('femaile', 'female')], null=True),
        ),
    ]
