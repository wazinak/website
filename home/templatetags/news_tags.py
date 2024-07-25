from django import template
from ..models import News

register = template.Library()


@register.inclusion_tag('latest_news.html')
def show_latest_news(count=5):
    latest_news = News.published.order_by('-publish')[:count]
    return {'latest_news': latest_news}
