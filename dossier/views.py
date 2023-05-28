import datetime
from urllib.parse import quote

import requests
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import *


def index(request):

    works = Project.objects.all()

    profile = Profile.objects.first()

    user = User.objects.filter(username='huzzy').first()

    skills = Skill.objects.all().order_by('-proficiency', 'name')[:5]

    blogs = get_news()[:4]

    context = {

        'profile': profile,
        'works': works,
        'me': user,
        'skills': skills,

        'blogs': blogs,

    }

    # messages.success(request, 'Welcome to the Future')
    return render(request, 'index.html', context)


def blog_posts(request):

    data = get_news()
    context = {
        'posts':  data,
        'profile': Profile.objects.first()

    }

    if request.method == "POST":
        keyword = request.POST.get("keyword")
        data = get_news(keyword)

        context.update(
            {
                "search": keyword,
                "posts": data
            }
        )

        return render(request, 'all_blog.html', context)

    return render(request, 'all_blog.html', context)


def get_news(keyword="Artificial intelligence"):
    url_safe_keyword = quote(keyword)
    url = f"https://newsdata.io/api/1/news?apikey=pub_23108e5a939d043e32812502c99aad60ae5bd&q={url_safe_keyword}&language=en&category=technology"

    response = requests.get(url)
    data = response.json()['results']

    for item in data:
        item['pubDate'] = datetime.datetime.strptime(
            item['pubDate'], "%Y-%m-%d %H:%M:%S")

    return data


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    profile = Profile.objects.first()
    context = {
        'post': post,
        'profile': profile,


    }
    return render(request, 'blog-detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            send_mail("New contact message",
                      "Check the database for new contact message", 
                      request.POST.get('email'), ["blazingkrane@gmail.com"])
            
            messages.success(request, 'Your Message has been sent succesfully')
            return redirect('/')
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.error(request, f'{field.name} | {error}')

                # Redirects back to the contact part of the page
                return redirect(f"{request.META['HTTP_REFERER']}#contact")


def add_blog(request):
    return redirect('admin:dossier_post_add')


def add_work(request):
    return redirect('admin:dossier_project_add')


def add_work(request):
    return redirect('admin:dossier_project_add')
