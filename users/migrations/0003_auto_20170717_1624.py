# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170717_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scientificuser',
            options={'permissions': (('read_car', 'Can read Car'),)},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
