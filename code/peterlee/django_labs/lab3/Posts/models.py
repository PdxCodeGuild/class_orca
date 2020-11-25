from django.db import models
from django.urls import reverse

class Posts(models.Model):
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Posts:detail', args=(self.id,))

    class Meta:
        ordering = ['-created']


