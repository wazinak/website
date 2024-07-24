from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import News


def index(request):
    return render(request, 'index.html')


def news_list(request):
    news = News.published.all()
    return render(request, 'news_list.html', {'news': news})


def news_detail(request, id):
    news = get_object_or_404(News, pk=id, status=News.Status.PUBLISHED)
    return render(request, 'news_detail.html', {'news': news})

