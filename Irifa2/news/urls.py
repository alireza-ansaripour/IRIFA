__author__ = 'alireza'
from django.conf.urls import patterns, url
from . import views


urlpatterns = [
               url(r'^$', views.home, name='home'),
               url(r'^article/(\w{1,30})/$', views.show_article),
               url(r'^news/(\w{1,2})/$', views.filter_news),
               ]