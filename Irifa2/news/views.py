# -*- coding: utf-8 -*-
from django.shortcuts import render

from news.models import News


__author__ = 'alireza'


def home(request):
    i_news = News.objects.filter(status='VERY_IMPORTANT')
    r_news = News.objects.filter(status='IMPORTANT')
    return render(request, "home.html", {'i_news': i_news, 'r_news': r_news,
                                         'title': u'پایگاه اینترنتی انجمن های دوستی ایران و سایر کشور ها'})


def show_article(request, id):
    news = News.objects.get(random_int=id)
    comments = news.comment_set.all()
    title = news.title
    return render(request, 'Show_news.html', {'news': news, 'title': title, 'can_edit': False})


def filter_news(request, continent):
    continents = {'as': "ASIA", 'na': "NORTH_AMERICA", 'sa': "SOUTH_AMERICA", 'eu': "EUROPE", 'af': "AFRICA",
                  'au': "AUSTRALIA"}
    all_news = News.objects.all()
    to_show = []
    for news in all_news:
        if news.continent() == continents[continent] and not news.status == 'NOT_IMPORTANT':
            to_show.append(news)

    return render(request, 'show_new_news.html', {'n_news': to_show})