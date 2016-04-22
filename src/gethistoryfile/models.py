from __future__ import absolute_import
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(user)
    slug = models.SlugField()
    sex = models.CharField(max_length=255)

    def__str__(self):
         return user

        class Meta:
            attach_together = ('user', 'sex')

class UrlOs(models.Model):
    os_name = models.CharField(max_length=255)
    os_version = models.CharField(max_length=255)
    os_kernel = models.CharField(max_length=255)

    def __str__(self):
        return ("Running {0}".format(os_name))

    class Meta:
        abstract = False

class BrowserDetails(models.Model):
    url_name = models.CharField(max_length=255)
    browser_name = models.CharField(max_length=255)
    browser_vender = models.CharField(max_length=255)
    time_viewd = models.CharField(max_length=255)
    checked = models.BooleanField(checked=True)
    search_engine = models.CharField(max_legnth=255) # like Google, MSN etc

    def __str__(self):
        return url_name

    class Meta:
        abstract = True
