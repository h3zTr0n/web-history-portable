# Author: Alison Mukoma
# aka capt10guts
#@                                   @#
# for assurity of sanity imports
from __future__ import absolute_import
from __future__ import unicode_literals

# calling useful packages
import getpass # Underlying module For user fetch
from datetime import datetime, timedelta
from django.shortcuts import render
from braces import views as Bviews
from django.views import generic
from binascii import *
from chardet import *
from string import *
import sys
import csv
import re
import os
import codecs
####base Page for activity.####
class HomeView(Bviews.LoginRequiredMixin, generic.TemplateView):
    template_name = "templates/gethistory/home.html"

# global function for
# getting computer user's username

def PcUser():
    try:
        user = getpass.getuser()
        # user = os.environ.get("USERNAME")
        return user
    except, Exception as e:
        return(str(e),+ ".Anonymous user agent.")


##############################33

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


class HistoryFileData(Bviews.LoginRequiredMixin):
    def __init__(self, *args, **kwargs):
            self.Butch_array = []
            self.array = []
            self.string = ""
            self.url = ""
            self.lines = []

    def removeNonAscii(string):
        url_line = ""
        for i in string:
            if(ord(i)==46 or ord(i)==47 or ord(i)==72 or ord(i) in range(97, 97+26) or ord(i) in range(65, 65+26)):
                url_line = url_line + i
            url_lines = url_line.split('\n')

            for url_line in url_lines:
                if url_line.startswith('http'):
                    print url_line.split('URL')[0]

        with open("C:\Users\PcUser\AppData\Local\Microsoft\Windows\History\History.IE5\MSHist012012030720120308\index.dat","r") as infile:
            for line in infile:
                batch_array = line.split("PcUser")

            for s in batch_array:
                removeNonAscii(s)
                return s



class LocateHistoryFile(object):

    def fetchHistoryFile(self):


        pattern = "(((http)|(https))(://)(www.)|().*?)\.[a-z]*/"

        SQL_STATEMENT = 'SELECT urls.url, visit_time FROM \
        visits, urls WHERE visits.url=urls.id;'

        storage = codecs.open('out.csv', 'w', 'utf-8')

        def date_from_webkit(webkit_timestamp):
        epoch_start = datetime.datetime(1601,1,1)
        delta = datetime.timedelta(microseconds=int(webkit_timestamp))
        return epoch_start + delta

        paths = ["~/Archived History", "~/History"]

        for path in paths:
        c = sqlite3.connect(path)
        for row in c.execute(SQL_STATEMENT):
            date_time = date_from_webkit(row[1])
            url = re.search(pattern, row[0])
            try:
                urlc = url.group(0)
            except:
                urlc = "ERROR"
            storage.write(str(date_time)[0:19] + "\t" + urlc + "\n")

    def senitizeFile(self):

    def filterData(self):

    def storeData(self):

    def store_to_json(self):

    def read_from_json(self):

    def store_to_db(self):

    def get_queryset(self):

#############################
st =  csv.re

        connection = sqlite3.connect(os.getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\history")
        connection.text_factory = str
        cur = connection.cursor()
        output_file = open('chrome_history.csv', 'wb')
        csv_writer = csv.writer(output_file)
        headers = ('URL', 'Title', 'Visit Count', 'Date (GMT)')
        csv_writer.writerow(headers)
        epoch = datetime(1601, 1, 1)
        for row in (cur.execute('select url, title, visit_count, last_visit_time from urls')):
            row = list(row)
            url_time = epoch + timedelta(microseconds=row[3])
            row[3] = url_time
            csv_writer.writerow(row)


            #################################################
            import os
import datetime
import sqlite3
import codecs, re

pattern = "(((http)|(https))(://)(www.)|().*?)\.[a-z]*/"

SQL_STATEMENT = 'SELECT urls.url, visit_time FROM visits, urls WHERE visits.url=urls.id;'

storage = codecs.open('out.csv', 'w', 'utf-8')

def date_from_webkit(webkit_timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(webkit_timestamp))
    return epoch_start + delta

paths = ["~/Archived History", "~/History"]

for path in paths:
    c = sqlite3.connect(path)
    for row in c.execute(SQL_STATEMENT):
        date_time = date_from_webkit(row[1])
        url = re.search(pattern, row[0])
        try: urlc = url.group(0)
        except: urlc = "ERROR"
        storage.write(str(date_time)[0:19] + "\t" + urlc + "\n")
#####################333
from collections import deque


class BrowserHistory(object, Bviews.LoginRequiredMixin):
    '''Class for keeping track of the history while moving
    to different locations, as implemented in Web browsers.

    Both back and forward history are supported and each of them can be bounded
    or unbounded.

    >>> h = BrowserHistory(max_back=3, max_forward=3)
    >>> h.location = 'http://www.google.com/'
    >>> h.location = 'http://www.python.org/'
    >>> h.location = 'http://xkcd.com/'
    >>> h.location = 'http://www.slashdot.org/'
    >>> h.location = 'http://www.digg.com/'
    >>> h.back()
    'http://www.slashdot.org/'
    >>> h.forward()
    'http://www.digg.com/'
    >>> h.go(-2)
    'http://xkcd.com/'
    >>> # max_back=3 so any result more than 3 pages back is deleted
    >>> for i_loc in h.indexed_locations():
    ...     print '%+d: %s' % i_loc
    +2: http://www.digg.com/
    +1: http://www.slashdot.org/
    +0: http://xkcd.com/
    -1: http://www.python.org/
    >>> # visiting a new location erases the forward history
    >>> h.location = 'http://en.wikipedia.org/'
    >>> for i_loc in h.indexed_locations():
    ...     print '%+d: %s' % i_loc
    +0: http://en.wikipedia.org/
    -1: http://xkcd.com/
    -2: http://www.python.org/
    '''

    def __init__(self, location=None, max_back=None, max_forward=None):
        '''Initialize a new BrowserHistory instance.

        :param location: If not None, the initial location.
        :param max_back: The maximum number of back locations to remember
            (default: no limit)
        :param max_forward: The maximum number of forward locations to remember
            (default: no limit)
        '''
        if max_back is not None:
            max_back += 1   # +1 for storing the current location
        self._back = deque(maxlen=max_back)
        self._forward = deque(maxlen=max_forward)
        if location is not None:
            self.location = location

    @property
    def location(self):
        '''The current location, i.e. the last location set or went to by
        :meth:`back`, :meth:`forward` or :meth:`go`.
        '''
        if self._back:
            return self._back[-1]
        raise AttributeError('location has not been set')

    @location.setter
    def location(self, value):
        '''Go to a new location. Any existing forward history is erased.'''
        self._back.append(value)
        self._forward.clear()

    def back(self, i=1):
        '''Jump to a location in history ``i`` steps back.

        :param i: The number of steps to jump back.
        :type i: positive int
        :returns: The current :attr:`location`.
        '''
        if i > 0:
            push_forward = self._forward.appendleft
            pop_back = self._back.pop
            for _ in xrange(min(i, len(self._back)-1)):
                push_forward(pop_back())
        return self.location

    def forward(self, i=1):
        '''Jump to a location in history ``i`` steps forward.

        :param i: The number of steps to jump forward.
        :type i: positive int
        :returns: The current :attr:`location`.
        '''
        if i > 0:
            push_back = self._back.append
            pop_forward = self._forward.popleft
            for _ in xrange(min(i, len(self._forward))):
                push_back(pop_forward())
        return self.location

    def go(self, i):
        '''Jump to a location in history ``i`` steps back or forward.

        :param i: The number of steps to jump forward (if positive) or back (if negative).
        :type i: int
        :returns: The current :attr:`location`.
        '''
        if i < 0:
            return self.back(-i)
        if i > 0:
            return self.forward(i)
        return self.location

    def indexed_locations(self):
        '''Return a list of ``(index,location)`` tuples for each location in history.

        The index ``i`` of a location ``l`` is defined so that ``go(i) == l``.
        Therefore indexes are positive for forward locations, negative for back
        locations and zero for the current :attr:`location`.
        '''
        result = []
        # back and current locations
        n = len(self._back)-1
        result.extend((i-n, location) for i,location in enumerate(self._back))
        # forward locations
        result.extend((i+1, location) for i,location in enumerate(self._forward))
        result.reverse()
        return result


if __name__ == '__main__':
    import doctest; doctest.testmod()
