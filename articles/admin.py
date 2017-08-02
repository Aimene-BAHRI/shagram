# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Categorie, Images
from users.models import CustomUser
# Register your models here.
class ProjectImageAdmin(admin.ModelAdmin):
    pass

class ProjectImageInline(admin.StackedInline):
    model = Images
    max_num=10
    extra=0


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'updated', 'posted', 'author']
    list_display_link = ['title']
    list_filter = ['categorie', 'posted', 'updated']
    inlines  = [ProjectImageInline,]
    class Meta:
        model = Article
        verbose_name = 'article'
        verbose_name_plural = 'articles'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}




admin.site.register(Article, BlogAdmin)
admin.site.register(Categorie, CategoryAdmin)
admin.site.register(Images, ProjectImageAdmin)
