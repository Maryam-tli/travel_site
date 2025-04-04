# Generated by Django 4.2.19 on 2025-03-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=220)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        default="Post_default/my_default.jpeg", upload_to="Post_default"
                    ),
                ),
                ("counted_views", models.IntegerField(default=0)),
                ("status", models.BooleanField(default=False)),
                ("published_date", models.DateTimeField(null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
