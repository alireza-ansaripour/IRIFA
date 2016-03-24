# -*- coding: utf-8 -*-
from persons.models import NGO
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class News(models.Model):
    class Meta:
        verbose_name = u'خبر'
        verbose_name_plural = u'اخبار'

    # random_int = models.CharField(primary_key=True, max_length=20)
    NGO = models.ForeignKey(NGO)
    title = models.CharField(verbose_name=u'تیتر', max_length=100)
    shortDescription = models.CharField(verbose_name=u'شرح مختصر', max_length=200)
    text = models.TextField(verbose_name=u'متن', )
    h_text = 'فرمت عکس باید با پسوند png باشد'
    picture = models.ImageField(verbose_name=u'عکس خبر',help_text=h_text, upload_to='News/pictures')
    date = models.DateField(verbose_name=u'تاریخ', )

    STATUSES = (
        ('NOT_SPECIFIED', u'نامعلوم'),
        ('VERY_IMPORTANT', u'خیلی مهم'),
        ('IMPORTANT', u'مهم'),
        ('NOT_IMPORTANT', u'مهم نیست'),
    )
    help_text = u'خبر های خیلی مهم در اسلایدر صفحه اصلی نشان داده می شوند' + '\n' + \
                u'!خبر های مهم در صفحه اصلی و در زیر اسلایدر به نمایش در خواهند امد' + '\n' + \
                u'!خبر هایی که مهم نیستند در صفحه اصلی نشان داده نمی شوند'
    status = models.CharField(max_length=30, choices=STATUSES, help_text=help_text, verbose_name=u'وضعیت')

    def continent(self):
        return self.NGO.continent

    def __str__(self):
        # return self.title.encode('utf-8')
        return self.title

class Comment(models.Model):
    News = models.ForeignKey(News)
    text = models.TextField(verbose_name=u'متن نظر', )
    date = models.DateField(verbose_name=u'تاریخ')
    show_it = models.BooleanField(verbose_name=u'نشان داده شود', )

    def __str__(self):
        return self.text




@receiver(pre_delete, sender=News)
def News_delete(sender, instance, **kwargs):
    News(instance).picture.delete(save=False)







