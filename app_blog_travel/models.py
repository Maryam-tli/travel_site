from django.db import models
from django.utils.text import slugify

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="author_default",default="first_img_author/author_info.jpeg" )
    about = models.TextField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to="Post_default",default="first_img_post/my_default.jpeg" )
    counted_views = models.IntegerField(default=0)
    Categories = models.ManyToManyField('category')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['published_date']
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)