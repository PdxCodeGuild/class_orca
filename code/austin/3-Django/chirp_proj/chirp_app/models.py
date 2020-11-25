from django.db import models
from django.urls import reverse
from users_app.models import CustomUser

    
class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=200)  
    post_text = models.TextField(default=None, blank=True)
    post_photo = models.ImageField(upload_to="images/")
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0)

    # def get_absolute_url(self):
    #     return reverse('chirp_app:detail', args=(self.id,))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    
    
    
