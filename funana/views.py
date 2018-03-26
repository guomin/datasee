# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView

from funana.models import *
import requests
import sys
from datetime import timedelta, date
import logging

#from utils import Utils

reload(sys)
sys.setdefaultencoding("utf-8")
__logger_name__ = "django.%s" % __name__
logger = logging.getLogger(__logger_name__)

def index(request):
    return render(request, "funana/index.html")

def iwd(request):
    return render(request, "funana/iwb.html")

def zhexian(request):
    #template = loader.get_template('funana/zhexian.html')
    #return HttpResponse(template.render(request, 'funana/zhexian.html'))
    return render(request, "funana/zhexian.html")

class BsFunnelStatsListView(ListView):
    model = BsFunnelStats
    template_name = 'funana/bs_funnel_stats_list.html'
    context_object_name = 'bs_funnel_stats_list'

    def get_queryset(self):
        end_time = self.request.GET.get('end_time', "")
        start_time = self.request.GET.get("start_time", "")
        default = ""
        if not end_time:
            end_time = default;
        if not start_time:
            start_time = default - timedelta(days=1)
        object_list = BsFunnelStats.objects.filter(date__gte=start_time, date__lte=end_time).order_by("-date")
        return object_list

    def get_context_data(self, **kwargs):
        context = super(BsFunnelStatsListView, self).get_context_data(**kwargs)
        end_time = self.request.GET.get("end_time", "")
        start_time = self.request.GET.get("start_time", "")
        default = ""
        context['end_time'] = end_time
        context['start_time'] = start_time
        return object_list
