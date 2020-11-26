
from django.db import models
from django.urls import reverse

class RagePage(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="images/", default = None, null = True)

    def get_absolute_url(self):
        return reverse('bloglab:detail', args=(self.id,))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
