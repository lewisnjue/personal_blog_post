from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='posts/images',blank=True)
    video = models.FileField(upload_to='posts/videos', blank=True, validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'webm', 'mkv'])])
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.ManyToManyField(User, related_name='comments', blank=True)
    