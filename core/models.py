from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Snippet(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=40)
    title = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.language}"