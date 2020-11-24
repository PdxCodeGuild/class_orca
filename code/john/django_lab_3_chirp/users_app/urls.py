# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 3, TWITTER MVP CLONE: https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab03-chirp.md
# PROJECT NAME: chirp_project
# APP NAMES: posts_app, users_app



from django.urls import path
from . import views

# THIS IS THE **USERS_APP** URLS.PY FILE
app_name = 'users_app'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
]
