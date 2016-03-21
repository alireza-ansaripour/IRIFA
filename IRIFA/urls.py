from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from IRIFA import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^', include("news.urls")),
                       url(r'^ngo/', include('persons.urls')),
#                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^summernote/', include('django_summernote.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': 'home'},
                           name='logout'),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
