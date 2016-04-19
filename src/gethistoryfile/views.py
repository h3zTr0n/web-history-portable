from __future__ import absolute_import
from django.shortcuts import render
from braces import views as Bviews
from django.views import generic
from os import *
from sys import *

# Create your views here.

class DetectOsPlatform(Bviews.LoginRequiredMixin,
                    Bviews.PermissionRequiredMixin):

    def __init__(self, *args , **kwargs):
        self.os_name = os_name
        self.os_version = os_version
        self.kernel_release = kernel_release

    def windows(self):
        try:
            pass
        except:
            continue

class DetectBrowserDetails(Bviews.LoginRequiredMixin):

    def __init__(self, *args, **kwargs):
        self.browser_name = browser_name # e.g Mozilla Firfox
        self.browser_vender = browser_vender # e.g netscap
        self.url = url  # url that was looked up i.e https://www.hackme.net/pentstrs/globintruders.cwd
        self.timestamp = timestamp # i.e when the url was searched / visited.
        self.user = user # i.e user that looked up that url
        self.search_engine = search_engine # e.g google_search_engine, MSN, Yahoo, Bing etc




class LocateHistoryFile(object):

    def fetchFile(self):

    def senitizeFile(self):

    def filterData(self):

    def storeData(self):
