from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)


class Profile(models.Model):
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    phone = models.CharField(max_length=15)
    image = models.URLField()
    brand_name = models.CharField(max_length=550)

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Skill (models.Model):
    name = models.CharField(max_length=550)
    proficiency = models.DecimalField(max_digits=3, decimal_places=1, validators=[
                                      MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self) -> str:
        return self.name


class Contact (models.Model):
    first_name = models.CharField(max_length=550)
    last_name = models.CharField(max_length=550)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    budget_level = models.CharField(max_length=250, blank=True, null=True)
    requirements = models.TextField()

    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name}'s Message"


class Project(models.Model):
    name = models.CharField(max_length=250)
    kind = models.CharField(max_length=250)
    image = models.URLField() 
    link = models.URLField()
    github_link = models.URLField()
    date_created =  models.DateTimeField(auto_now_add=True)
    date_updated  = models.DateTimeField( auto_now=True)
 
    def __str__(self) -> str:
        return self.name


class Post (models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True)
    slug = models.SlugField(editable=False)
    title = models.CharField(max_length=550)
    content = models.TextField()
    image = models.ImageField(upload_to='blog')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=500, null=True)
    link = models.URLField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(**kwargs)

    def __str__(self) -> str:
        return self.title
