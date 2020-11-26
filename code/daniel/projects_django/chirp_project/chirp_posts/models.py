from django.db import models
from django.urls import reverse 


class ChirpPosts(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True) 
    likes = models.IntegerField(default=0)
    media = models.ImageField(upload_to="images/")

    def get_absolute_url(self):
        return reverse("chirp_posts:detail", args=(self.id,)) 
    
    # def __repr__(self):
    #     return self.content

    def __str__(self):
        return self.content 

    class Meta: 
        ordering = ['-created_on'] 

class LikedPosts(models.Model):
    post = models.ForeignKey(ChirpPosts, on_delete=models.CASCADE)
    liked_by = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    is_liked = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.post
