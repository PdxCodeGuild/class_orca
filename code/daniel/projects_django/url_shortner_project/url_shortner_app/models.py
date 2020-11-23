from django.db import models


class urlCode(models.Model):
    url_code = models.CharField(max_length=50)
    url_name = models.CharField(max_length=200)
    url = models.TextField()
    url_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.url_code

class METAData(models.Model):
    ip = models.CharField(max_length=200)
    server_name = models.CharField(max_length=200)
    server_port = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ip
    
    
