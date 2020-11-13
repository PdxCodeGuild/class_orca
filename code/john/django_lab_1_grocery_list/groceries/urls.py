# LAB 1, GROCERY LIST
# THIS IS THE PROJECT FOLDER
# groceries is the project name
# grocery_list is the 'app' name, only one in this proj

"""groceries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groceries/', include('grocery_list.urls')), # app name, 
    # PUT ALL APPS HERE
    # first thing is the URL, whatever you want
    # second thing is the thing to include
]
