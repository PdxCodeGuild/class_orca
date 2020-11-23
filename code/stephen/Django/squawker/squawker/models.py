from django.db import models
from django.urls import reverse

class Squeek(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="images/", blank=True, null=True)

    def get_absolute_url(self):
        return reverse('squawker:detail', args=(self.id,))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']