# Generated by Django 5.0.7 on 2024-07-24 06:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_news_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-publish']},
        ),
        migrations.RemoveIndex(
            model_name='news',
            name='home_news_publish_b0e018_idx',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='published',
            new_name='publish',
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['-publish'], name='home_news_publish_6b9ee5_idx'),
        ),
    ]
