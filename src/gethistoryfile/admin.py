from __future__ import absolute_import

from django.contrib import admin
from .models import UrlStore
# Register your models
class SignUpAdmin(admin.ModelAdmin):
    """docstring for SignUpAdmin"""
    list_display = ["__unicode__", "url", "date_visited", "search_text", "user"]
    # def __init__(self):
    #     super(SignUpAdmin, self).__init__()
    class Meta:
        model = UrlStore

admin.site.register(UrlStore, SignUpAdmin)
