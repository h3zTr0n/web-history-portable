from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from braces import views
from . import models

# Create your views here.


class TalkListDetailView(generic.View):

    def get(self, request, *args, **kwargs):

            return HttpResponse('A talk list')


class TalkListDetailView(views.LoginRequiredMixin,
  views.PrefetchRelatedMixin,
  generic.DetailView
  ):
    model = models.TalkList
    prefetch_related = ('talks')

        # Author: Alison Mukoma a.k.a # Capt10Guts #
        #Linux CodeWriter
def get_queryset(self):
        queryset = super(TalkListDetailView, self).get_queryset()
        queryset = queryset.filters(user=self.self.request.user)
        return queryset

class TalkListListView(views.LoginRequiredMixin,
 generic.ListView):
    models = models.TalkList

    def get_queryset(self):
        return self.request.user.lists.all()

# class HomePageView(generic.TemplateView):
#     template_name = 'talklist_list.html'
#
# from __future__ import absolute_import
# from django.contrib.auth.decorators import login_required
# from django.generic import views
# from braces import views as bViews
# from . import models
# from . import forms
