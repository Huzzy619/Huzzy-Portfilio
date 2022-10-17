# Generated by Django 4.1.2 on 2022-10-14 10:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("dossier", "0005_rename_name_contact_first_name_contact_last_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(editable=False)),
                ("title", models.CharField(max_length=550)),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="blog")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
