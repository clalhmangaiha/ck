from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg',upload_to='profile_pics/')
    bio = models.TextField(blank=True)
    cover_photo = models.ImageField(default='mizomade_cover.jpg',upload_to='cover_pics/')

    def __str__(self):
        return f'{self.name.username}'
    
class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='follower',on_delete=models.CASCADE)
    following = models.ForeignKey(User,related_name='following',on_delete=models.CASCADE)