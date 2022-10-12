from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique = True)

class Profile(models.Model):
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    phone = models.CharField(max_length = 15)
    image = models.ImageField(upload_to = 'profile')
    brand_name = models.CharField(max_length = 550)

    user = models.OneToOneField(User, on_delete = models.CASCADE)

class Skill (models.Model):
    name = models.CharField(max_length = 550)
    proficiency = models.DecimalField(max_digits = 3, decimal_places =1, validators = [MinValueValidator(0), MaxValueValidator(100)] )

    def __str__(self) -> str:
        return self.name


class Contact (models.Model):
    name = models.CharField(max_length = 550)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length = 15)
    budget_level = models.CharField(max_length = 250)
    requirements = models.TextField()

    created_on = models.DateTimeField(auto_now = True)


class Project(models.Model):
    name = models.CharField(max_length = 250)
    kind = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'works')
    link = models.URLField()

    def __str__(self) -> str:
        return self.name