# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 5, BLOG https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab05-blog.md
# PROJECT NAME: blog_project
# APP NAMES: blog_app, users_app


from django.urls import path

from . import views

# this urls.py is in the app folder
app_name = 'blog_app'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('blog_app/new/', views.BlogCreateView.as_view(), name='new_post'),
    path('blog_app/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('blog_app/<int:pk>/edit/', views.BlogEditView.as_view(), name='edit_post'),
    path('blog_app/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete_post'),
]