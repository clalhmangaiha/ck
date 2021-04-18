# from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

# class Article(models.Model):
#     title=models.CharField('Title', max_length=200)
#     text=CKEditor5Field('Text', config_name='extends')

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
# from modelcluster.fields import ParentalManyToManyField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,null=True)
    categoryimage = models.ImageField(upload_to='assets/',null=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    Author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    title = models.CharField(max_length=500,null=True)
    slug = models.SlugField(max_length=500,null=True,blank=True)
    coverimage = models.ImageField(upload_to='image/',null=True,blank=True)
    
    

    intro = models.CharField(max_length=200,null=True)
    category = models.ManyToManyField(Category,related_name='categories',null=True,blank=True)
    content = CKEditor5Field('Text', config_name='extends',blank=True)
    tags = TaggableManager(blank=True)

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.title)
        
        super(Post,self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.Author.username}'

    # def save_model(self, request, obj, form, change):
    #     obj.added_by = request.user
    #     super().save_model(request, obj, form, change)    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='postcomments')
    commented_on = models.DateTimeField(auto_now_add=True,null=True)
    commenter = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comment = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.commenter.username} - {self.post}'

class Bookmark(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="users_bookmark")
    post = models.ManyToManyField(Post,null=True)
    
    def __str__(self):
        return self.user.username

class Activity(models.Model):
    post = models.ForeignKey(Post, related_name="activity",on_delete=models.CASCADE,null=True)
    user = models.TextField(default=None)
    def __str__(self):
        return f'{self.user}-{self.post}'

