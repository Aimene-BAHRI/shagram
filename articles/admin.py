# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Categorie
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'updated', 'posted']
    list_display_link = ['title']
    list_filter = ['categorie', 'posted', 'updated']
    class Meta:
        model = Article
        verbose_name = 'article'
        verbose_name_plural = 'articles'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, BlogAdmin)
admin.site.register(Categorie, CategoryAdmin)
