# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-30 14:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20170726_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='slug',
        ),
    ]
