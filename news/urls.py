__author__ = 'alireza'
from django.conf.urls import patterns, url

urlpatterns = patterns('news.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^article/(\w{1,30})/$', 'show_article'),
                       url(r'^news/(\w{1,2})/$', 'filter_news'),
                       )