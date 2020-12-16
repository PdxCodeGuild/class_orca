# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 5, BLOG https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab05-blog.md
# PROJECT NAME: blog_project
# APP NAMES: blog_app, users_app

from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # see model field reference, : 
        # SET() # sending to foster care to see where should go next
        # SET_NULL # forgot
        # SET_DEFAULT # kids to orphanage
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) # useful, lookup
    
    # DON'T MAKE TOO MANY MIGRATIONS AT ONCE...SMALL CHANGES!
    # body = models.TextField()
    # caption = models.TextField()
    caption = models.CharField(max_length=500)

    photo = models.ImageField(upload_to="media/")
    # also see models.FileField    

    def get_absolute_url(self):
        # posts from urls.py, posts_app
        return reverse('blog_app:detail', args=(self.id,))
        # merrit's working:
        # # return reverse('posts:detail', args=(self.id,)) 
        # 
    

    def __str__(self):
        return self.title
        # return f'{self.title}, created {self.created}.'
        # NOTE how this works

    class Meta:
        ordering = ['-created']


# Could make a form here:
# class Form(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True) # useful, lookup
#     body = models.TextField()

#     def __str__(self):
#         return self.title
