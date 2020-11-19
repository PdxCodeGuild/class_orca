from django.db import models

import random
import string

class UrlChanger(models.Model):
    long_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    clicked = models.IntegerField(default=0)
    linked_from = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.long_url



    # def short_url(self):
    #     characters = string.ascii_letters + string.digits
    #     new_url = "urlchanger/"
    #     for x in range(5):
    #         new_url += random.choice(characters)
    #     return new_url


# import random
# import string

# characters = string.ascii_letters + string.digits + string.punctuation
# password = random.choice(characters)

# for x in range(9):
#     password += random.choice(characters)

# print(f'You\'re new random password is: {password}')