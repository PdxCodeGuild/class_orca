# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 5, BLOG https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab05-blog.md
# PROJECT NAME: blog_project
# APP NAMES: blog_app, users_app


# users_app 
from django.contrib import auth # auth is for the users_app
from django.urls import path

from . import views

app_name = 'users_app'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
    # path('admin/', admin.site.urls),
    # path('user/', include('django.contrib.auth.urls')), # big debate user or users
    # path('user/', include('users_app.urls')), # big debate user or users
    # path('', include(), name=''),
    # path('', include('blog_app.urls')),
]