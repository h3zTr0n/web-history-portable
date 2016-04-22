from __future__ import absolute_import

from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
url(r'^', views.ShowHistory.as_view(), name='ShowHistory'),
]
