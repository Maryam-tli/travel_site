# Generated by Django 4.2.19 on 2025-04-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_blog_travel", "0002_author_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="about",
            field=models.TextField(default="No bio yet"),
            preserve_default=False,
        ),
    ]
