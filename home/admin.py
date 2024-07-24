from django.contrib import admin
from .models import News


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'status', 'author']
    list_filter = ['created']
    prepopulated_fields = {'slug': ('title',)}
