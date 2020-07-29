from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class User(models.Model):
    username= models.CharField(max_length=150)
    password= models.PasswordField(max_length=20)
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.username