# POLLS EXAMPLE PROJECT

from django.db import models
from django.utils import timezone

import datetime 

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # old: # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

# id
# text
# when published

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # missing number of votes, so that's what this line does

    # remember this gives the cute, printed version
    def __str__(self):
        return self.choice_text

