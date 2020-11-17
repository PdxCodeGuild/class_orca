# LAB 1, GROCERY LIST
# THIS IS THE APP FOLDER
# groceries is the project name
# grocery_list is the 'app' name, only one in this proj

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

# THIS IS THE APP FOLDER! 

from django.urls import path

from . import views

app_name = 'grocery_list'

urlpatterns = [    
    # GENERALLY  GO FROM *MORE* SPECIFIC TO LEAST SPECIFIC...
    # path, then function, then NAME of path
    
    # INDEX PAGE:
    path('', views.index, name='index'),
    
    path('add_item/', views.add_item, name='add_item'),
    path('mark_completed/', views.mark_completed, name='mark_completed'),
    path('mark_incomplete/', views.mark_completed, name='mark_incomplete'),
    path('delete_item/', views.delete_item, name='delete_item'),

    path('update_or_delete/', views.update_or_delete, name='update_or_delete'),
]
