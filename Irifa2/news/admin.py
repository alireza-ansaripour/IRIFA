# -*- coding: utf-8 -*-
import os
import datetime
from django.contrib.admin.actions import delete_selected

from django.utils.crypto import get_random_string
from PIL import Image
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.translation import ugettext_lazy as _

from Irifa2.settings import BASE_DIR
from news.models import News, Comment
from persons.models import Expert


class Comment_inline(admin.TabularInline):
    extra = 0
    model = Comment
    list_display = ('News', 'text', 'date', 'show_it', )
    readonly_fields = ('text', 'date', 'News')

class StatusFilter(admin.SimpleListFilter):
    title = u'بر اساس انواع خبر ها'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('NOT_SPECIFIED', _(u'نامعلوم')),
            ('VERY_IMPORTANT', _(u'خیلی مهم')),
            ('IMPORTANT', _(u'مهم')),
            ('NOT_IMPORTANT', _(u'بررسی شده')),
        )

    def queryset(self, request, queryset):
        if request.user.is_superuser:
            if self.value() == 'NOT_SPECIFIED':
                return News.objects.filter(status = 'NOT_SPECIFIED')
            elif self.value() == 'VERY_IMPORTANT':
                return News.objects.filter(status = 'VERY_IMPORTANT')
            elif self.value() == 'IMPORTANT':
                return News.objects.filter(status = 'IMPORTANT')
            elif self.value() == 'NOT_IMPORTANT':
                return News.objects.filter(status = 'NOT_IMPORTANT')
        elif request.user.is_superuser is False :
            if self.value() == 'NOT_SPECIFIED':
                return News.objects.filter(NGO__expert__person = request.user, status = 'NOT_SPECIFIED')
            elif self.value() == 'VERY_IMPORTANT':
                return News.objects.filter(NGO__expert__person = request.user, status = 'VERY_IMPORTANT')
            elif self.value() == 'IMPORTANT':
                return News.objects.filter(NGO__expert__person = request.user, status = 'IMPORTANT')
            elif self.value() == 'NOT_IMPORTANT':
                return News.objects.filter(NGO__expert__person = request.user, status = 'NOT_IMPORTANT')


def make_important(modeladmin, request, queryset):
    queryset.update(status='IMPORTANT')
make_important.short_description = u'تغییر وضعیت به مهم'


def make_Vimportant(modeladmin, request, queryset):
    queryset.update(status='VERY_IMPORTANT')
make_Vimportant.short_description = u'تعییر وضعیت به بسیار مهم'


def make_nimportant(modeladmin, request, queryset):
    queryset.update(status='NOT_IMPORTANT')
make_nimportant.short_description = u'تغییر وضعیت به دیده شده'





class Comment_inline(admin.TabularInline):
        extra = 0
        model = Comment
        list_display = ('News', 'text', 'date', 'show_it', )
        readonly_fields = ('text', 'date', 'News')

class News_admin(admin.ModelAdmin):

    readonly_fields = ('NGO', 'date', )
    list_display = ('NGO', 'title', 'shortDescription', 'text', 'picture', 'date', 'status')
    list_display_links = ('title', )
    exclude = ('random_int',)
    inlines = (Comment_inline,)
    # actions = [delete_selected]
    list_filter = (StatusFilter, )

    def get_actions(self, request):
        actions = super(News_admin, self).get_actions(request)
        if not request.user.is_superuser:
            return actions
        else:
            self.actions.append(make_Vimportant)
            self.actions.append(make_important)
            self.actions.append(make_nimportant)
        return actions



    def get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display
        else:
            return 'title', 'shortDescription', 'text', 'picture'

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return 'NGO', 'title', 'shortDescription', 'text', 'picture', 'date'
        else:
            return 'NGO', 'date', 'status'

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if change:
                if not request.user.is_superuser:
                    if 'picture' in form.changed_data:
                        news = News.objects.get(id=obj.id)
                        news.picture.delete(save=False)
            else:
                ngo = request.user.ngo_expert.NGO
                obj.NGO = ngo
            print('before date')
            obj.date = datetime.date.today()
            obj.save()



            # if change:
            #     if 'picture' in form.changed_data:
            #         news = News.objects.get(id=obj.id)
            #         news.picture.delete(save=False)
            #         obj.save()
            #         return
            # if change and request.user.is_superuser:
            #     # obj.status = form.cleaned_data['status']
            #     obj.save()
            #     return
            # file = os.path.join(BASE_DIR, 'media/News/thumbnails/')
            # expert = Expert.objects.get(person=request.user)
            # obj.NGO = expert.NGO
            # obj.date = datetime.date.today()
            # pic = form.cleaned_data['picture']
            # unique_id = get_random_string()
            # if not change:
            #     obj.random_int = unique_id
            #     pic.name = unique_id + '.jpg'
            # else:
            #     if not form.cleaned_data['picture'] == pic.name:
            #         pic.name = unique_id + '.jpg'
            # obj.picture = pic
            # obj.save()
            # path = os.path.join(BASE_DIR,'media/News/thumbnails/'+ pic.name[pic.name.rfind('/')+1::])
            # image = Image.open(path)
            # size = 160, 120
            # image.thumbnail(size)
            # image.save(file+unique_id+'.png', 'PNG')


admin.site.register(News, News_admin)
