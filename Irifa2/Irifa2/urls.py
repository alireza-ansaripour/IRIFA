from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import django
from Irifa2 import settings

admin.autodiscover()

urlpatterns =[
               url(r'^', include("news.urls")),
               url(r'^ngo/', include('persons.urls')),
               url(r'^summernote/', include('django_summernote.urls')),
               url(r'^admin/', include(admin.site.urls)),
               # url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': 'home'}, name='logout'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
