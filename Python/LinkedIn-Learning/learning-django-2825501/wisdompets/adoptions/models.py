from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = (('M','Male'), ('F','Female'))
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    vaccinations = models.ManyToManyField('vaccine', blank=True)

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  
        return self.name