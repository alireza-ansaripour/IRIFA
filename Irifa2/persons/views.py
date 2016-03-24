from django.shortcuts import render
from news.models import News
from persons.models import NGO, ImageNGO

__author__ = 'alireza'


def show_NGO(request, name):
    ngo = NGO.objects.get(latin_name=name)
    news = News.objects.filter(NGO=ngo)[0:4]
    photos = ImageNGO.objects.filter(NGO=ngo)[0:4]
    title = ngo.persian_name
    return render(request, 'NGO/news_archive.html',
                  {'page_title': name, 'ngo': ngo, 'r_news': news, 'pics': photos, 'title': title})
