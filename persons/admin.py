# -*- coding: utf-8 -*-
import os
from PIL import Image
import django_summernote
from IRIFA.settings import BASE_DIR
from .models import NGO, Expert, ImageNGO

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin

# admin.site.unregister(django_summernote)


class ContinentFilter(admin.SimpleListFilter):
    title = 'بر اساس قاره ها'
    parameter_name = 'continent'

    def lookups(self, request, model_admin):
        return (
            ('آسیا', _('ASIA')),
            ('آفریقا', _('AFRICA')),
            ('اروپا', _('EUROPE')),
            ('آمریکای شمالی', _('NORTH_AMERICA')),
            ('آمریکای جنوبی', _('SOUTH_AMERICA')),
            ('استرالیا', _('AUSTRALIA')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'ASIA':
            return NGO.objects.filter(continent='ASIA')
        elif self.value() == 'AFRICA':
            return NGO.objects.filter(continent='AFRICA')
        elif self.value() == 'EUROPE':
            return NGO.objects.filter(continent='EUROPE')
        elif self.value() == 'NORTH_AMERICA':
            return NGO.objects.filter(continent='NORTH_AMERICA')
        elif self.value() == 'SOUTH_AMERICA':
            return NGO.objects.filter('SOUTH_AMERICA')
        elif self.value() == 'AUSTRALIA':
            return NGO.objects.filter('AUSTRALIA')


class ImageNGO_inline(admin.TabularInline):
    model = ImageNGO
    extra = 1


class NGO_admin(SummernoteModelAdmin):

    list_display = ('persian_name', 'latin_name', 'continent', )
    list_display_links = ('persian_name',)
    list_filter = (ContinentFilter, )
    search_fields = ['persian_name', 'latin_name' ]
    ordering = ('persian_name',)

    def get_queryset(self, request):
        qs = super(NGO_admin, self).get_queryset(request)
        if request.user.is_superuser :
            return qs
        else:
            return NGO.objects.filter(expert=request.user.ngo_expert)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        else:
            return 'persian_name', 'latin_name', 'continent'

    def save_model(self, request, obj, form, change):

        if form.is_valid():
            file = os.path.join(BASE_DIR, 'media/NGO/thumbnails/')
            pic = form.cleaned_data['flag']
            if not change:
                name = form.cleaned_data['latin_name']
            else:
                name = obj.latin_name
            pic.name = name + '.jpg'
            obj.flag = pic
            obj.save()
            path = '/home/alireza/Desktop/IRIFA/media/NGO/flags/' + pic.name
            image = Image.open(path)
            size = 200, 170
            image.thumbnail(size)

            image.save(file+name+'.png', 'PNG')

admin.site.register(NGO, NGO_admin)




admin.site.register(Expert)
