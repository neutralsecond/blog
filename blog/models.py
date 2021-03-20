from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Favorites(models.Model):
    blogger = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="blogger", on_delete=models.CASCADE)
    favorite = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="favorite", on_delete=models.CASCADE)