from __future__ import absolute_import

from django.conf.urls import patterns, url, include
from . import views

lists_patterns = [
    url(r'^$', views.TalkListListView.as_view(), name='list'),
    url(r'^d/ (?P<slug>[-\w]+)/$', views.TalkListDetailView.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^lists/', include(lists_patterns, namespace='lists')),
]
