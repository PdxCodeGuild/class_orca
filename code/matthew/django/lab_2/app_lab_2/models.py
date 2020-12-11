from django.db import models

class Main (models.Model):
    code_text = models.CharField(max_length=6)
    url_text = models.TextField(max_length=200)
    click_count = models.IntegerField(default=0)

    # to be connected in the views
    def __str__(self):
        return f' code: {self.code_text}, url: {self.url_text}' 

    