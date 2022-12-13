from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField



class User(AbstractUser):
    phone = models.CharField(max_length=10,unique = True,null= True,blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    profile = models.TextField(null = True,blank = True,default=None) 
    country = models.CharField(max_length=50,null = True)
    is_Author = models.BooleanField(default=False)
    avatar  = models.ImageField(blank = True,null=True,default = None,upload_to='uploads/%Y/%m',)

# BaseItem: parent class which is inherited by 
#           Authors, Administrators, Members
# class User(AbstractUser): 
#     class Meta:
#         abstract = True
#     #username = models.CharField(max_length=20, unique=True)
#     #password = models.CharField(max_length=20)
#     #name = models.CharField(max_length=50,null=False)
#     #birthdate = models.DateField(null=False,default=None)
#     phone = models.CharField(max_length=10,unique = True,null= True,blank=True)
#     #date_joined = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     #active = models.BooleanField(default=True)  # active: show status of account, 1-ACTIVE, 0-DELETE
#     #email = models.CharField(max_length=50,null = False,unique=True)

# class Authors(User):
#     img = models.ImageField(null = True,upload_to = 'authors/%Y/%m',default=None)
#     profile = models.TextField(null = True,blank = True,default=None)
#     country = models.CharField(max_length=50,null = False,default=None)


# class Administrators(User):
#     profile = models.TextField(null = True,blank = True)
#     img = models.ImageField(null = True,upload_to = 'admins/%Y/%m',default=None)    

# class Members(User):
#     display_name = models.CharField(max_length=50,null=False,default=None)
#     img = models.ImageField(null = True,upload_to = 'members/%Y/%m',default=None)

#---------------------------------------------------------------------------------------------
class Subscriber(models.Model):
    email = models.CharField(max_length=50,null = False,unique=True)
    active = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=50,null = False,unique= True)
    description = models.TextField(null = True,blank=True)
    articles = models.ManyToManyField('Article',related_name='category_articles')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Subscriber_Category(models.Model):
    subscriber = models.ForeignKey(Subscriber,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    class Meta:
        unique_together = (('subscriber','category'),)
    subscribed_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) #active: show status of subscriber with their Category, 1-ACTIVE, 0-DELETE

class Article(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null = True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null= True)
    title =  models.CharField(max_length=100,null = False)
    content = RichTextField(null = False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False) #active: show status of Article, 1-PUBLISHED, 0-CHECKING

    def __str__(self):
        return self.title

class Images_Article(models.Model):
    Article = models.ForeignKey(Article,on_delete = models.CASCADE,null=False,default=None)
    imgTitle = models.CharField(max_length=100,null=False,default=None)
    img = models.ImageField(null=False,upload_to='Article/%Y/%m')
    class Meta:
        unique_together = (('Article','imgTitle'),)

class Comment(models.Model):
    context = models.TextField(null = False)
    date_posted = models.DateTimeField(auto_now_add=True)
    like_number = models.IntegerField(default=0)
    dislike_number = models.IntegerField(default=0)
    admin = models.ForeignKey(User,related_name = 'admin_comment',on_delete=models.SET_NULL,null=True)
    commentor = models.ForeignKey(User,related_name = 'commentor_comment',on_delete=models.SET_NULL,null=True)
    Article = models.ForeignKey(Article,on_delete=models.CASCADE,default = None)
    active = models.BooleanField(default=True) #active: show status of comment, 1-ACTIVE, 0-DELETE