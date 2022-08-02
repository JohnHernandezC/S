# Generated by Django 4.0.1 on 2022-07-30 03:21

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0004_remove_usuarios_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='username',
            field=models.CharField(default=None, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]
