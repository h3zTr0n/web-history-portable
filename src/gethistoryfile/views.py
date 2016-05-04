# Author: Alison Mukoma
# aka capt10guts

from __future__ import absolute_import

from braces import views as Bviews
from django.views import generic
import getpass
from . import models
from django.http import Http404

def PcUser(self):
    try:
        self.user = getpass.getuser()
        # user = os.environ.get("USERNAME")
        return str(user)
    except Exception as e:
        return(str(e),+ ".Anonymous user agent.")

class HomeView(generic.TemplateView):
    """docstring for HomeView"""
    template_name = "templates/gethistory/home.html"

class LinuxPathToHistoryFile(object):
    """docstring for LinuxPathToistoryFile"""
    def __init__(self, *args, **kwargs):
        super(LinuxPathToistoryFile, self).__init__()
        self.path = "/home/PcUser/.mozilla/firefox/bo0bkrwm.default-1362842976106/places.sqlite"

        import sqlite3

    def readAndSendToModel(self):
        data = self.path
        readFromDb = sqlite3.connect("places.sqlite")
        cur = readFromDb.cursor()
        columns = cur.execute(" SELECT datetime(moz_historyvisits.visit_date/1000000,'unixepoch'), moz_places.url, title  FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id \
                              ")
        for col in columns:
            modelCol = models.UrlStore.Create(col)
            modelCol.save()

class UrlDetailView(generic.DetailView):
    """docstring for UrlDetailView"""
    def __init__(self):
        super(UrlDetailView, self).__init__()

        # Get the name of a slug field to be used to look up by slug.
    def get_slug_field(self):
        return self.slug_field

        # Return the `QuerySet` that will be used to look up the object.
    def get_queryset(self):
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.all()
            else:
                raise ImproperlyConfigured(
                   "%(cls)s is missing a QuerySet. Define "
                   "%(cls)s.model, %(cls)s.queryset, or override "
                   "%(cls)s.get_queryset()." % {
                       'cls': self.__class__.__name__
                   }
                  )
        return self.queryset.all()


    # Returns the object the view is displaying.

    def get_object(self):
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView

        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError("Generic detail view %s must be called with"
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)
        try:

            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._metz_verbose_name})
        return obj








    # SELECT datetime(moz_historyvisits.visit_date/1000000,'unixepoch'), moz_places.url
    # FROM moz_places, moz_historyvisits
    # WHERE moz_places.id = moz_historyvisits.place_id



# class DetectOsPlatform(Bviews.LoginRequiredMixin,
#                     Bviews.PermissionRequiredMixin):
#
#     def __init__(self, *args , **kwargs):
#         self.os_name = os_name
#         self.os_version = os_version
#         self.kernel_release = kernel_release
#
#     def windows(self):
#         try:
#             pass
#         except:
#             pass

# class DetectBrowserDetails(Bviews.LoginRequiredMixin):


# class HistoryFileData(Bviews.LoginRequiredMixin):
#     def __init__(self, *args, **kwargs):
#             self.Butch_array = []
#             self.array = []
#             self.string = ""
#             self.url = ""
#             self.lines = []
#     def removeNonAscii(string):
#         url_line = ""
#         for i in string:
#             if(ord(i)==46 or ord(i)==47 or ord(i)==72 or ord(i) in range(97, 97+26) or ord(i) in range(65, 65+26)):
#                 url_line = url_line + i
#             url_lines = url_line.split('\n')
#
#             for url_line in url_lines:
#                 if url_line.startswith('http'):
#                     print url_line.split('URL')[0]
#
#         with open("C:\Users\PcUser\AppData\Local\Microsoft\Windows\History\History.IE5\MSHist012012030720120308\index.dat","r") as infile:
#             for line in infile:
#                 batch_array = line.split("PcUser")
#
#             for s in batch_array:
#                 removeNonAscii(s)
#                 return s
#



#############################
# st =  csv.re
#
#         connection = sqlite3.connect(os.getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\history")
#         connection.text_factory = str
#         cur = connection.cursor()
#         output_file = open('chrome_history.csv', 'wb')
#         csv_writer = csv.writer(output_file)
#         headers = ('URL', 'Title', 'Visit Count', 'Date (GMT)')
#         csv_writer.writerow(headers)
#         epoch = datetime(1601, 1, 1)
#         for row in (cur.execute('select url, title, visit_count, last_visit_time from urls')):
#             row = list(row)
#             url_time = epoch + timedelta(microseconds=row[3])
#             row[3] = url_time
#             csv_writer.writerow(row)
