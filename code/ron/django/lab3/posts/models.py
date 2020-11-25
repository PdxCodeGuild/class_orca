from django.db import models
from django.urls import reverse


class Post(models.Model):
    ''' Database structure '''
    title   = models.CharField(max_length=50)
    # Note the ForeignKey, used to link to another table in db 
    author  = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body    = models.CharField(max_length=100)
    photo   = models.ImageField(upload_to="images/", null=True, blank=True)

    # Returns the user back to a designated area after updating the database
    def get_absolute_url(self):
        return reverse('posts:entry', args=(self.id,))

  # Returns a string to viewer (i.e. in admin page)
    def __str__(self):
        return self.title

    # Class Meta internal to django, ordering [] is the default method by 
    #   which items will be displayed (can utilize sub-items as well)
    class Meta:
        ordering = ['-created', '-author']