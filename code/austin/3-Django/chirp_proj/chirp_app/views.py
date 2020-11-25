from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Post
from emails.models import Signup

def index(request):
    featuredset = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-created')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featuredset,
        'latest': latest
    }
    print(context, "CONTEXT*******")
    return render(request, 'chirp_app/index.html', context)

def blog(request):
    post_list = Post.objects.all()

    context = {
        'post_list': post_list
    }
    return render(request, 'chirp_app/blog.html', context)

def post(request):
    return render(request, 'chirp_app/post.html', {})
