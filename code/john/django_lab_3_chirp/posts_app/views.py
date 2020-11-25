# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 3, TWITTER MVP CLONE: https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab03-chirp.md
# PROJECT NAME: chirp_project
# APP NAMES: posts_app, users_app

# django urls stuff
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

# django views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# django auth stuff
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm # from https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
from django.contrib.auth.decorators import login_required # from the djangogirls tutorial for the comment check

# our post model
from .models import Post, Comment
from .forms import CommentForm # , PostForm
    # i don't have a postform do i?

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'

    fields = ['post_text' ] # add 'photo' if media

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # CreateView has a form_valid() function...
        # super means ... before you do what you were going to do anyway... let me add something

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['post_text']

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'

    success_url = reverse_lazy('posts_app:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


# from https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html :
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # "an important bit is to call update_session_auth_hash() after you save the form. Otherwise the user’s auth session will be invalidated and she/he will have to log in again."
            messages.success(request, 'Your password was successfully updated. Horray for security!')
            return redirect('posts_app:change_password')
            # next try posts_app:change_password
            # why not return to user profile page?
        else:
            messages.error(request, 'Please correct the below error:')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

# # # # # # # # # # # # # # # # # # # # # # # # 
# WORKING ON COMMENT SYSTEM ... 
# 
# Notes from Merritt convo: 
# - comment system
# 	- or, more complicated (something else? What was it...)
# 	- foreign key (or keys?)
# 	- thinking about/working with DB is good
# 	- do whichever is more of a challenge
# 
# FROM https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab05-blog.md
    # Comment
    #         user: a many-to-one relationship to the User table
    #         blogpost: foreign reference to blogpost
    #         body: text of the comment's body
    #         timestamp: when the comment was made
    # Pages
    # These pages should be protected, meaning the views which serve them should check the permissions of the user attempting to access them.
    #     Post List: Show only the post title, username, and the timestamp.
    #     Post Detail: Show the post title, username, and timestamp, as well as the body and the comments. Each comment should show the user, the timestamp, and the comment body. The comment section should also have a text area for users to enter new comments.
    #     Make Post: Allow posters to create new posts.
# 
# https://subscription.packtpub.com/book/web_development/9781784391911/2/ch02lvl1sec19/creating-a-comment-system
# To build the comment system, you will need to:
#     Create a model to save comments
#     Create a form to submit comments and validate the input data
#     Add a view that processes the form and saves the new comment into the database
#     Edit the post detail template to display the list of comments and the form for adding a new comment
# 
# 
# https://djangocentral.com/creating-comments-system-with-django/
# a littlo old, says Django 2.x app, good to view but

# https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/
# 
# 
# # # # # # # # # # # # # # # # # # # # # # # # 


# # THIS SECTION SHOULD BE INSIDE FORMS.PY, IMPORTED HERE INTO VIEWS...
# from .models import Post, Comment

# class CommentForm(forms.ModelForm):
    
#     class Meta:
#         model = Comment
#         fields = ('author', 'comment_text')
# # ...END SECTION

# add_comment_to_post
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":

        form = CommentForm(request.POST)

        # DOES THIS NEED TO IMPORT SOMETHING I DON'T HAVE?
        if form.is_valid(): 

            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts_app:detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'new_comment.html', {
        'form' : form
    })

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('posts_app:detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('posts_app:detail', pk=comment.post.pk)



