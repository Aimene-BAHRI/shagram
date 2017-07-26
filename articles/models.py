# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
# Create your models here.
def upload_location(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "articles/post_images/%s/%s" %(slug, filename)

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(db_index=True, auto_now_add=False, auto_now=True) 
    categorie = models.ForeignKey('articles.Categorie', default=1)
   
    def __unicode__(self):
        return '%s' % self.title
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id" : self.id})

    class Meta:
        ordering = ["-posted", "-updated"]

class Images(models.Model):
    post = models.ForeignKey(Article, default = None) 
    image = models.ImageField(upload_to = upload_location, verbose_name='Image')

class Categorie(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title

