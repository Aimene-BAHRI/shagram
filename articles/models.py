# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.contrib import admin
from django.template.defaultfilters import slugify

LANGUAGES = (
    ('FRENCH','Fr'),
    ('ARABE','Ar'),
    ('ENGLISH','En'),
)

def upload_location(instance, filename):
    title = instance.post.title
    slug =  slugify(title)
    return "articles/post_images/%s/%s" %(slug, filename)

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(db_index=True, auto_now_add=False, auto_now=True) 
    categorie = models.ForeignKey('articles.Categorie', default=1)
    sources = models.TextField(null = True)
    document = models.FileField(blank = True, null = True)
    language = models.CharField(max_length = 60,choices=LANGUAGES, default = 'ARABE')
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id" : self.id})

    class Meta:
        ordering = ["-posted", "-updated"]

class Categorie(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique = True)

    def __str__(self):
        return self.title

class Images(models.Model):
    image = models.ImageField(upload_to = upload_location, verbose_name='Image')
    post = models.ForeignKey(Article, default = None) 

