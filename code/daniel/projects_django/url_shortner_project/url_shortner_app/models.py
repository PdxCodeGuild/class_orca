from django.db import models


class urlCode(models.Model):
    url_code = models.CharField(max_length=50)
    url_name = models.CharField(max_length=200)
    url = models.TextField()

    def __str__(self):
        return self.url_code


    
