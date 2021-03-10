from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    pass



class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40)
    user_image = models.ImageField(upload_to='images', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('developer-profile', args=[str(self.id)])

    def __str__(self):
        return f'{self.user}'


        
class Snippet(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=40)
    title = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True, related_name='snippets')

    def __str__(self):
        return f"{self.user} | {self.title} | {self.language}"
