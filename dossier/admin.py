from django.contrib import admin
from .models import Post, Profile, Contact, Project, Skill, User

# Register your models here.

admin.site.register([User, Profile, Contact, Project, Skill, Post])
