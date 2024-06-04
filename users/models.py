
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='user/profilepic', blank=True)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followed_by')
    following = models.ManyToManyField('self', symmetrical=False, related_name='follows')

