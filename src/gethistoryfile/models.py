from __future__ import absolute_import
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
# Create your models here.

class UrlOs(models.Model):
    os_name = models.CharField(max_length=255)
    os_version = models.CharField(max_length=255)
    os_kernel = models.CharField(max_length=255)

def __str__(self):
    return ("Running {0}".format(os_name))

class Meta:
    abstract = False
        
