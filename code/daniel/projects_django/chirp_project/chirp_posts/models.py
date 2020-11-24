from django.db import models
from django.urls import reverse 


class ChirpPosts(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True) 

    def get_absolute_url(self):
        return reverse("chirp_posts:detail", args=(self.id,)) 
    

    def __str__(self):
        return self.content 

    class Meta: 
        ordering = ['-created_on'] 