from django.db import models
from users.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    decription = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images/')
    user = models.ForeignKey(User, related_name='post_user', on_delete=models.CASCADE)