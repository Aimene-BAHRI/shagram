# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 14:52
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20170723_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='no-image.png', upload_to=articles.models.upload_location),
        ),
    ]
