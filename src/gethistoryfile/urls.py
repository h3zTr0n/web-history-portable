from __future__ import absolute_import

from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
url(r'^home/activity', views.HomeView.as_view(), name="activity"),
]
