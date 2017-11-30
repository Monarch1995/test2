from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=75)
    url = models.URLField(blank=True)
    text = models.TextField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text