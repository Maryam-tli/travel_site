# Generated by Django 4.2.19 on 2025-04-19 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog_travel', '0006_alter_author_image_alter_post_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Tags',
            new_name='category',
        ),
    ]
