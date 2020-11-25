# LAB 3: CHIRP TWITTER MVP CLONE, 
# THIS IS THE APP POSTS_APP FOLDER
# project name is CHIRP_PROJECT 
 
from django.contrib import admin

from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)