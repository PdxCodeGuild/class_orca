from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import Post


def home(request):
    posts_list = Post.objects.order_by('created')
    context = {'posts_list': posts_list }
    return render(request, 'posts/home.html', context)

def login_page(request):
    return render(request, 'posts/login.html')

def login_key(request):
    print("*" * 30)
    print(request.POST)
    print("*" * 30)
    username = request.POST['id_input']
    password = request.POST['pass_input']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse( 'posts:home'))
    else:
        return HttpResponseRedirect(reverse( 'posts:login'))

def register_page(request):
    return render(request, 'posts/register.html')

def register_key(request):
    print("*" * 30)
    print(request.POST)
    create_id = request.POST['id_input']
    create_password = request.POST['pass_input']
    User.objects.create_user( username=create_id, password=create_password)
    return HttpResponseRedirect(reverse( 'posts:home'))

def logout_key(request):
    logout(request)
    return HttpResponseRedirect(reverse( 'posts:home'))

def submit_key(request):
    title_field = request.POST['title_key']
    body_field = request.POST['blog_key']
    Post.objects.create(title=title_field, body=body_field, author=request.user)
    return HttpResponseRedirect(reverse('posts:home'))

def update_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post,}
    return render(request, 'posts/update.html', context)

# @login_required
def update_key(request, pk):
    update_post = get_object_or_404(Post, pk=pk)
    title = request.POST['title_key']
    body = request.POST['blog_key']
    update_post.body = body 
    update_post.title = title
    update_post.save()
    return HttpResponseRedirect(reverse('posts:home'))

# @login_required    
def delete_key(request,pk):
    delete_post = get_object_or_404(Post, pk=pk)
    delete_post.delete()
    return HttpResponseRedirect(reverse('posts:home'))

# def user_check(user):
#     return user.user