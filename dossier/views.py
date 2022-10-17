from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContactForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
# @login_required(login_url='login')


def index (request):

    works = Project.objects.all()

    profile  = Profile.objects.first()

    user = User.objects.filter(username = 'huzzy').first()

    skills = Skill.objects.all().order_by('-proficiency', 'name')[:5] 

    blogs = Post.objects.order_by('-date_created')[:4]

    print(request.META['HTTP_HOST'])

    context = {

        'profile' : profile,
        'works' : works,
        'me' : user, 
        'skills': skills,

        'blogs': blogs,

    }

    # messages.success(request, 'Welcome to the Future')
    return render (request, 'index.html', context )

def blog_posts(request):
    context = { 
        'posts': Post.objects.all().order_by('-date_created'),
        'profile'  : Profile.objects.first()
    }
    return render (request, 'all_blog.html', context)

def blog_detail (request, slug):
    post  = get_object_or_404(Post, slug=slug)
    profile  = Profile.objects.first()
    context = {
    'post': post,
    'profile' : profile,

 
    }
    return render (request, 'blog-detail.html', context )

def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your Message has been sent succesfully')
            return redirect ('/')
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.error(request, f'{field.name} | {error}')

                return redirect(f"{request.META['HTTP_REFERER']}#contact") # Redirects back to the contact part of the page


def add_blog (request):
    return redirect('admin:dossier_post_add')

def add_work(request):
    return redirect('admin:dossier_project_add')

