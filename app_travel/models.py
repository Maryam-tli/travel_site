from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    image = models.ImageField(upload_to="Post_default",default="Post_default/my_default.jpeg" )
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['published_date']
        
    def __str__(self):
        return self.title