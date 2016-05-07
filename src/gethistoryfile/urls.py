from __future__ import absolute_import

from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
url(r'activities', views.ActivitiesView.as_view(), name="home"),
url(r'^table/data', views.MyDataView.as_view(), name='data_table'),
]
