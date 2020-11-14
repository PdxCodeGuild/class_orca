# POLLS EXAMPLE PROJECT
# URLs from poll APP folder

from django.urls import path
from . import views

app_name = 'polls' # kinda a 'magic' variable that we had to also change in the index.html thing

# CLASS BASED VIEWS:
urlpatterns = [ # this urlpatterns MUST BE EXACT!
    # GENERALLY  GO FROM *MORE* SPECIFIC TO LEAST SPECIFIC...
    path('', views.IndexView.as_view(), name='index'), # path, then function, then NAME of path
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # could be str:string here to look for a string URL
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]

# old URL patterns, FUNCTION BASED VIEWS:
# urlpatterns = [ # this urlpatterns MUST BE EXACT!
#     path('', views.index, name='index'), # path, then function, then NAME of path
#     path('<int:question_id>/', views.detail, name='detail'),
#     # could be str:string here to look for a string URL
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]

# COPIED FROM URLS.PY IN PROJECT FOLDER:
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

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""