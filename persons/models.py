# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User,Permission
# from ckeditor.fields import RichTextField


class NGO(models.Model):
    class Meta:
        verbose_name = 'انجمن دوستی'
        verbose_name_plural = 'انجمن ها'
    persian_name = models.CharField(max_length=100, verbose_name="نام فارسی")
    latin_name = models.CharField(max_length=100, verbose_name="نام لاتین", unique=True)

    CONTINENTS = (
        ("NORTH_AMERICA", 'آمریکای شمالی'),
        ("SOUTH_AMERICA", 'آمریکای جنوبی'),
        ("ASIA", 'آسیا'),
        ("EUROPE", 'اروپا'),
        ("AFRICA", 'افریقا'),
        ("AUSTRALIA", 'استرالیا'),
    )
    continent = models.CharField(max_length=30, choices=CONTINENTS)

    flag = models.ImageField(verbose_name='پرچم', upload_to='NGO/flags')
    about_country = models.TextField(verbose_name='درباره کشور', )
    about_NGO = models.TextField(verbose_name='درباره انجمن', )

    def __str__(self):
        return self.latin_name



class ImageNGO(models.Model):
    class Meta:
        verbose_name = u'عکس'
        verbose_name_plural = u'عکس های گالری'
    NGO = models.ForeignKey(NGO, related_name='gallery')
    Image = models.ImageField(upload_to='NGO/Gallery', verbose_name='فایل')
    description = models.TextField(verbose_name='توضیحات')
    @property
    def filename(self):
        return os.path.basename(self.file.name)

class Expert(models.Model):
    class Meta:
        verbose_name = u'کارشناس'
        verbose_name_plural = u'کارشناسان'
    person = models.OneToOneField(User, null=True, blank=True, related_name='ngo_expert')
    NGO = models.OneToOneField(NGO, null=True)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.person.is_staff = True

        pers = [32, 33, 20, 22, 23, 24, 31]
        for permission in pers:
            p1 = Permission.objects.get(id=permission)
            self.person.user_permissions.add(p1)

        self.person.save()
        super(Expert, self).save()
    def __str__(self):
        return self.person.first_name + " " + self.person.last_name + " expert of NGO " + self.NGO.latin_name
