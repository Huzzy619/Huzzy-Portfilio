from django.urls import path
from .views import add_work, index, contact, blog_detail, blog_posts, add_blog
from django.contrib.auth.views import LoginView
urlpatterns = [

    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('blogs', blog_posts, name='blog_posts'),
    path('blog/post/<slug:slug>', blog_detail, name='blog_detail'),
    path('add/post', add_blog, name='add_blog'),
    path('add/work', add_work, name='add_work'),

    path('login', LoginView.as_view(template_name='login.html'), name='login'),
]
