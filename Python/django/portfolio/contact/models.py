from django.db import models

# Create your models here.


class contact(models.Model):
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
