from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django import forms


class User(AbstractUser):
    avatar  = models.ImageField(upload_to='uploads/%Y/%m')


# BaseItem: parent class which is inherited by 
#           Authors, Administrators, Members
class BaseItem(models.Model):
    class Meta:
        abstract = True
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50,null=False)
    birthdate = models.DateField(null=False,default=None)
    phone = models.CharField(max_length=10,unique = True,null= True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)  # active: show status of account, 1-ACTIVE, 0-DELETE
    email = models.CharField(max_length=50,null = False,unique=True)

class Authors(BaseItem):
    img = models.ImageField(null = True,upload_to = 'authors/%Y/%m',default=None)
    profile = models.TextField(null = True,blank = True,default=None)
    country = models.CharField(max_length=50,null = False,default=None)


class Administrators(BaseItem):
    profile = models.TextField(null = True,blank = True)
    img = models.ImageField(null = True,upload_to = 'admins/%Y/%m',default=None)    

class Members(BaseItem):
    display_name = models.CharField(max_length=50,null=False,default='No name')
    img = models.ImageField(null = True,upload_to = 'members/%Y/%m',default=None)

#---------------------------------------------------------------------------------------------
class Subscribers(models.Model):
    email = models.CharField(max_length=50,null = False,unique=True)

class Categories(models.Model):
    name = models.CharField(max_length=50,null = False,unique= True)
    description = models.TextField(null = True,blank=True)

    def __str__(self):
        return self.name

class Subscribers_Categories(models.Model):
    subscriber = models.ForeignKey(Subscribers,related_name = 'subscriber',on_delete=models.CASCADE)
    category = models.ForeignKey(Categories,related_name = 'category',on_delete=models.CASCADE)
    class Meta:
        unique_together = (('subscriber','category'),)
    subscribed_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) #active: show status of subscribers with their categories, 1-ACTIVE, 0-DELETE

class News(models.Model):
    category = models.ForeignKey(Categories,related_name = 'news_category',on_delete=models.SET_NULL, null = True)
    author = models.ForeignKey(Authors,related_name = 'news_author',on_delete=models.SET_NULL, null= True)
    title =  models.CharField(max_length=100,null = False)
    content = RichTextField(null = False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) #active: show status of news, 1-ACTIVE, 0-DELETE

    def __str__(self):
        return self.title

class Images_News(models.Model):
    news = models.ForeignKey(News,related_name='image_news',on_delete = models.CASCADE,null=False,default=None)
    imgTitle = models.CharField(max_length=100,null=False,default=None)
    img = models.ImageField(null=True,upload_to='news/%Y/%m')
    class Meta:
        unique_together = (('news','imgTitle'),)

class Comments(models.Model):
    context = models.TextField(null = False)
    date_posted = models.DateTimeField(auto_now_add=True)
    like_number = models.IntegerField(default=0)
    dislike_number = models.IntegerField(default=0)
    admin = models.ForeignKey(Administrators,related_name = 'admin',on_delete=models.SET_NULL,null=True)
    commentor = models.ForeignKey(Members,related_name = 'member',on_delete=models.SET_NULL,null=True)
    news = models.ForeignKey(News,related_name = 'comment_news',on_delete=models.CASCADE,default = None)
    active = models.BooleanField(default=True) #active: show status of comment, 1-ACTIVE, 0-DELETE