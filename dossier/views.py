from django.shortcuts import render
from .models import *

# Create your views here.

def index (request):

    works = Project.objects.all()

    profile  = Profile.objects.first()

    user = User.objects.filter(username = 'huzzy').first()

    skills = Skill.objects.all().order_by('name')

    context = {

        'profile' : profile,
        'works' : works,
        'me' : user, 
        'skills': skills

    }
    return render (request, 'index.html', context )