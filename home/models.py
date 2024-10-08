from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db import models
from services.utils import unique_slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.PUBLISHED)


class News(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = "published",
        DRAFT = "draft",
    title = models.CharField(max_length=250, verbose_name="Название новости")
    slug = models.SlugField(max_length=250, verbose_name="Идентификатор новости", blank=True)
    body = models.TextField(verbose_name="Текст новости")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT, verbose_name="Статус новости")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='home_news',
                               default=None)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:new_detail', args=[self.publish.year, self.publish.month,self.publish.day, self.slug])

    def save(self, *args, **kwargs):
        self.slug = unique_slugify(self, self.title, self.slug)
        super().save(*args, **kwargs)
