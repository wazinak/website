from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models


class News(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = "published",
        DRAFT = "draft",
    title = models.CharField(max_length=250, verbose_name="Название новости")
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField(verbose_name="Текст новости")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT, verbose_name="Статус новости")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='home_news',
                               default=None)

    class Meta:
        ordering = ['-published']
        indexes = [models.Index(fields=['published'])]

    def __str__(self):
        return self.title
