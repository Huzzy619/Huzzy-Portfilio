from ninja import Schema, ModelSchema
from dossier.models import Skill, Post, Profile
from pydantic import EmailStr


class ProjectSchema(Schema):
    id: int
    name: str
    kind: str
    image: str
    link: str


class ContactSchema(Schema):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    budget_level: str
    requirements: str


class SkillSchema(ModelSchema):
    class Config:
        model = Skill
        model_fields = "__all__"


class PostSchema(ModelSchema):
    class Config:
        model = Post
        model_fields = "__all__"


class ProfileSchema(ModelSchema):
    class Config:
        model = Profile
        model_exclude = ["user", "id"]
