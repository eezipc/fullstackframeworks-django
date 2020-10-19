from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# Blog Models Class


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('bikeblog',)
