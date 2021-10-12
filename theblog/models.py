from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=250)
    header_image = models.ImageField(null = True,blank=True,upload_to="images/")
    title_tag = models.CharField(max_length=250,default='Welcome To TheBlog')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    posting_date = models.DateField(auto_now_add=True)
    body = RichTextField(blank=True,null=True)
    #body = models.TextField()
    category = models.CharField(max_length=255,default='other')
    likes = models.ManyToManyField(User,related_name='blog_posts',blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title +'|'+str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-detail',args = (str(self.id)))
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to = "images/profile",null=True,blank = True)
    Mobile = models.CharField(max_length=11,default="")
    wb_url = models.CharField(max_length=250,null=True,blank=True)
    insta_url = models.CharField(max_length=250,null=True,blank=True)
    twitter_url = models.CharField(max_length=250,null=True,blank=True)
    fb_url = models.CharField(max_length=250,null=True,blank=True)
    whatsapp_url = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return str(self.user)

    

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete = models.CASCADE)
    author = models.CharField(max_length=100)
    commented_on = models.DateField(auto_now_add=True)
    body = models.TextField(null=True,blank=True)

    def total_comments(self):
        return self.post.count()

    def __str__(self):
        return str(self.post.title) + str(  self.body)

   
        