from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index-with-base', views.iwb, name='index-with-base'),
    url(r'^zhexian/$', views.zhexian, name='zhexian'),
]
