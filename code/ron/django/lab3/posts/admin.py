# this is where you tell django about your 
#   superuser and database

from django.contrib import admin

from .models import Post

admin.site.register(Post)
