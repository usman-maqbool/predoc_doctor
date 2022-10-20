# Generated by Django 3.2.9 on 2022-10-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_remove_usermodel_qr_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('is_agree', models.BooleanField(default=False)),
            ],
        ),
    ]
