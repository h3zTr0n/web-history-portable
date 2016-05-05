# Author: Alison Mukoma
# a.k.a cap10guts

from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify
# Create your models here.

CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
class User(models.Model):
    user = models.CharField(max_length=255)
    slug = models.SlugField()
    sex = models.CharField(choices=CHOICES, max_length=2)

    def __str__(self):
         return user

    class Meta:
        unique_together = (('user', 'sex',))

class UrlOs(models.Model):
    os_name = models.CharField(max_length=255)
    os_version = models.CharField(max_length=255)
    os_kernel = models.CharField(max_length=255)

    def __str__(self):
        return ("Running {0}".format(os_name))

class UrlStore(models.Model):
    url = models.URLField()
    date_searched = models.DateTimeField(auto_now_add=False)
    last_visited = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

# fetchng from model dar
class ReadUrlModelData(object):
    """docstring for ReadUrlModelData"""
    def __init__(self, arg):
        super(ReadUrlModelData, self).__init__()
        self.arg = arg


# class BrowserDetails(models.Model):
#     url_name = models.CharField(max_length=255)
#     browser_name = models.CharField(max_length=255)
#     browser_vender = models.CharField(max_length=255)
#     time_viewd = models.CharField(max_length=255)
#     checked = models.BooleanField(checked=True)
#     search_engine = models.CharField(max_legnth=255) # like Google, MSN etc
#
#     def __str__(self):
#         return url_name
