# LAB 2, URL SHORTENER. NAMES: URL_PROJECT AND URL_APP.

from django.contrib import admin

# Register your models here.

from .models import URL

admin.site.register(URL)