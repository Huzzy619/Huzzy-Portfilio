import datetime
from urllib.parse import quote

import requests
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Post, Profile, Project, Skill, User


def index(request):
    works = Project.objects.all().order_by("-priority")

    profile = Profile.objects.first()

    user = User.objects.filter(username="huzzy").first()

    skills = Skill.objects.all().order_by("-proficiency", "name")[:5]

    blogs = get_news()[:4]

    pictures_set = get_images()

    context = {
        "profile": profile,
        "works": works,
        "me": user,
        "skills": skills,
        "blogs": blogs,
        "pictures": pictures_set,
    }

    # messages.success(request, 'Welcome to the Future')
    return render(request, "index.html", context)


def blog_posts(request):
    data = get_news()
    pictures = get_images(count=(len(data) if len(data) < 30 else 10))

    context = {"posts": data, "profile": Profile.objects.first(), "pictures": pictures}

    if request.method == "POST":
        keyword = request.POST.get("keyword")
        data = get_news(keyword)
        pictures = get_images(
            count=(len(data) if len(data) < 30 else 10), query=keyword
        )

        context.update({"search": keyword, "posts": data, "pictures": pictures})

        return render(request, "all_blog.html", context)

    return render(request, "all_blog.html", context)


def get_news(keyword="Artificial intelligence"):
    url_safe_keyword = quote(keyword)
    url = f"https://newsdata.io/api/1/news?apikey=pub_23108e5a939d043e32812502c99aad60ae5bd&q={url_safe_keyword}&language=en&category=technology"

    response = requests.get(url)
    data = response.json()["results"]

    for item in data:
        item["pubDate"] = datetime.datetime.strptime(
            item["pubDate"], "%Y-%m-%d %H:%M:%S"
        )

    return data


def get_images(count=4, query="Artificial intelligence"):
    headers = {"Accept-Version": "v1"}
    params = {"count": count, "orientation": "portrait", "query": query}
    resp = requests.get(
        url=f"https://api.unsplash.com/photos/random/?client_id={settings.UNSPLASH_ACCESS_KEY}",
        headers=headers,
        params=params,
    )

    pictures = resp.json()

    pictures_set = [picture["urls"]["regular"] for picture in pictures]

    return pictures_set


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    profile = Profile.objects.first()
    context = {
        "post": post,
        "profile": profile,
    }
    return render(request, "blog-detail.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            send_mail(
                "New contact message",
                "Check the database for new contact message",
                request.POST.get("email"),
                ["blazingkrane@gmail.com"],
            )

            messages.success(request, "Your Message has been sent successfully")
            return redirect("/")
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.error(request, f"{field.name} | {error}")

                # Redirects back to the contact part of the page
                return redirect(f"{request.META['HTTP_REFERRER']}#contact")


def add_blog(request):
    return redirect("admin:dossier_post_add")


def add_work(request):
    return redirect("admin:dossier_project_add")
