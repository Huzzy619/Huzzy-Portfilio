from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from dossier.models import Profile, Project, Contact, Post, Skill

from .schema import ContactSchema, PostSchema, ProjectSchema, SkillSchema

api = NinjaAPI()


@api.get('/profile')
def get_profile(request):
    profile = Profile.objects.first()
    return profile


@api.get('/projects', response=list[ProjectSchema])
def get_projects(request):
    projects = Project.objects.all()
    return projects


@api.get("/skills", response=list[SkillSchema])
def my_skills(request):
    skills = Skill.objects.all().order_by('-proficiency', 'name')[:5]

    return skills


@api.post("/contact")
def contact_me(request, info: ContactSchema):
    Contact.objects.create(**info.dict())

    return {
        "detail": "Message sent successfully",
        "status": True
    }


@api.get('/posts', response=list[PostSchema])
def blog_posts(request):
    posts = Post.objects.all().order_by('-date_created')

    return posts


@api.get("/post/{post_id}", response=PostSchema)
def single_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)

    return post
