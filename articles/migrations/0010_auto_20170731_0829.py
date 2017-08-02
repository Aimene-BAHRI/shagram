# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-31 08:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0009_remove_images_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='article',
            name='language',
            field=models.CharField(choices=[('FRENCH', 'Fr'), ('ARABE', 'Ar'), ('ENGLISH', 'En')], default='Ar', max_length=60),
        ),
        migrations.AddField(
            model_name='article',
            name='sources',
            field=models.TextField(null=True),
        ),
    ]