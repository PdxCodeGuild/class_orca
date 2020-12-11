from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.body, self.title
        return self.title