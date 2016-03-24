__author__ = 'alireza'
from django.conf.urls import patterns, url
from . import views

urlpatterns =[
               url(r'^(\w{1,30})/$', views.show_NGO),
             ]