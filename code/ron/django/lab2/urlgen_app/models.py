
from django.db import models
from django.utils import timezone

import datetime
 
class url(models.Model):
    url_long = models.CharField(max_length=50)
    url_short = models.CharField(max_length=5)
    created_date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.url_long
        # returns string instead of object type



    # def was_created_recently(self):
    # now = timezone.now()
    # return now - datetime.timedelta(days=1) <= self.created_date <= now