from django.db.models import Count
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import Post, Category
from emails.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset

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
    return render(request, 'chirp_app/index.html', context)

def blog(request):
    category_list = Category.objects.all()
    post_list = Post.objects.all()
    most_recent = Post.objects.order_by('-created')[:3]
    paginator = Paginator(post_list, 4)
    page_request_var = 'page' 
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_list': category_list
    }
    return render(request, 'chirp_app/blog.html', context)

def post(request, id):
    return render(request, 'chirp_app/post.html', {})





