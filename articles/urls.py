"""shagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import index, post_create, post_detail, post_update, post_delete

urlpatterns = [
    # List of all articles
    url(r'^$', view=index, name='index'),

    # Create an article
    url(r'^create/$', view=post_create, name='create'),

    # Detail of an article
    url(r'^(?P<id>\d+)/$', view=post_detail, name='detail'),

    # Update an article
    url(r'^update/(?P<id>\d+)/$', view=post_update, name='update'),

    # Delete an article
    url(r'^delete/(?P<id>\d+)$', view=post_delete, name='delete'),
]

