# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, "funana/index.html")

def zhexian(request):
    #template = loader.get_template('funana/zhexian.html')
    #return HttpResponse(template.render(request, 'funana/zhexian.html'))
    return render(request, "funana/zhexian.html")
