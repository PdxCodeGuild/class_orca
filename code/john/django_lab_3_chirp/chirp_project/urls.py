# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 3, TWITTER MVP CLONE: https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab03-chirp.md
# PROJECT NAME: chirp_project
# APP NAMES: posts_app, users_app


# lab 3: chirp website, this is the urls.py in CHIRP_PROJECT , app is posts_app
# THIS IS THE **PROJECT** URLS.PY FILE

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')), # users plural, not user
    path('users/', include('users_app.urls')),
    path('', include('posts_app.urls')), # NOTE I SET THIS TO ROOT, NOT 'posts_app/' # NOTE CHANGED BACK...
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # only necessary if using media...
