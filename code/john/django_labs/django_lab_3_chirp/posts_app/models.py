
# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 3, TWITTER MVP CLONE: https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab03-chirp.md
# PROJECT NAME: chirp_project
# APP NAMES: posts_app, users_app

from django.db import models
from django.urls import reverse

class Post(models.Model):
    post_text = models.CharField(max_length=80)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)    
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True) # useful, lookup
    

    # photo = models.ImageField(upload_to="media/")
    # DON'T MAKE TOO MANY MIGRATIONS AT ONCE...SMALL CHANGES!
    # also see models.FileField    

    def get_absolute_url(self):
        return reverse("posts_app:detail", args=(self.id,))
    

    def __str__(self):
        return self.post_text

    class Meta:
        ordering = ['-created']

class Comment(models.Model):
    post = models.ForeignKey('posts_app.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=60)
    comment_text = models.CharField(max_length=60) # 'text' in the djangogirls docs...

    created = models.DateField(auto_now_add=True) # 'created_date' in the djangogirls docs...
    # note used DateField with auto_now_add and NOT DateTimeField like the djangogirls docs...

    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_text

