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
