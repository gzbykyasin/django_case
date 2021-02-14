from django.db import models
from django.utils import timezone
from django.db.models.fields import ( DateField,CharField,TextField,FloatField,TimeField,DateTimeField,IntegerField)
from django.db import migrations
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True,help_text="Post title")
    slug = models.SlugField(max_length=255, unique=True,help_text="Post slug")
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts',help_text="Post author")
    updated_on = models.DateTimeField(auto_now= True,help_text="Post updated date")
    image = models.ImageField(upload_to='',help_text="Post image")
    content = RichTextField(help_text="Post content")
    created_on = models.DateTimeField(auto_now_add=True,help_text="Post created date")
    status = models.IntegerField(choices=STATUS, default=0,help_text="Post status")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title