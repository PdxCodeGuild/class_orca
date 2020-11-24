from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Post

def index(request):
    queryset = Post.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    print(context, "CONTEXT*******")
    return render(request, 'chirp_app/index.html', context)

def blog(request):
    return render(request, 'chirp_app/blog.html', {})

def post(request):
    return render(request, 'chirp_app/post.html', {})
