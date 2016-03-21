__author__ = 'alireza'
from django.conf.urls import patterns, url

urlpatterns = patterns('persons.views',
                       url(r'^(\w{1,30})/$', 'show_NGO'),
                       )