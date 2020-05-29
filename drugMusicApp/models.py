from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=10)
    nick = models.CharField(max_length=10)
    photo = models.ImageField()

class Video(models.Model):
    profile = models.ForeignKey(profile, on_delete=models.CASCADE, related_name="videos")
    link = models.CharField(max_length = 100)