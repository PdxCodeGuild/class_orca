from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.Charfield(max_length=250)
    author = models.Charfield(max_length=100)
    isbn = models.Charfield(max_length=13) #easier to keep this field Char vs. Int -> not math and leading zeros are an issue
                                           #    Easier to keep zip codes, cc numbers, etc. as text vs. numbers

    def __str__(self):
        return self.title
        

