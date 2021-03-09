from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile (models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    username = models.CharField(max_length=40)
    user_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user}"
        
class Snippet(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=40)
    title = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True, related_name='snippets')

    def __str__(self):
        return f"{self.user} | {self.code}"

       