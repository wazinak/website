from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import News


def index(request):
    return render(request, 'index.html')


def new_list(request):
    new_list = News.published.all()
    paginator = Paginator(new_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        news = paginator.page(page_number)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'news': news})


def new_detail(request, year, month, day, new):
    new = get_object_or_404(News, status=News.Status.PUBLISHED,
                            slug=new,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    return render(request, 'detail.html', {'new': new})

