from django.db import models
from django.urls import reverse
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.username


class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
