# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 5, BLOG https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab05-blog.md
# PROJECT NAME: blog_project
# APP NAMES: blog_app, users_app

from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)