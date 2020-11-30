# Generated by Django 3.1.3 on 2020-11-25 22:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('squawker', '0009_auto_20201124_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='squeek',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
