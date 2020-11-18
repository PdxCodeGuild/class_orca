# LAB 2, URL SHORTENER. NAMES: URL_PROJECT AND URL_APP.
# THIS IS THE URL_APP URLS.PY FILE

"""polls_project URL Configuration

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

from django.urls import path

from . import views

app_name = 'url_app'

# THIS IS THE URL_APP FOLDER! 

urlpatterns = [    # GENERALLY  GO FROM *MORE* SPECIFIC TO LEAST SPECIFIC: path, then function, then NAME of path
    path('', views.index, name='index'),
    path('generate_short_code/', views.generate_short_code, name='generate_short_code'),
    path('<str:code>/', views.redirect_code_to_URL, name='redirect_code_to_URL'),       # # # # # # # bottom of list
]