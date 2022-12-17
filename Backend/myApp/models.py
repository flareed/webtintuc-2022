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

class Category(models.Model):
    name = models.CharField(max_length=50,null = False,unique= True)
    description = models.TextField(null = True,blank=True)
    #articles = models.ManyToManyField('Article',related_name='category_articles')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    subscriber = models.CharField(max_length=50,null = False,unique=True)
    categories = models.ManyToManyField('Category',related_name = 'categories')
    active = models.BooleanField(default=True) #active: show status of subscriber with their Category, 1-ACTIVE, 0-DELETE

    class Meta:
        ordering = ['subscriber']

class Article(models.Model):
    category = models.ForeignKey(Category,related_name = "articles", on_delete=models.SET_NULL, null = True)
    author = models.CharField(max_length=100, null= True)
    title =  models.CharField(max_length=100,null = False)
    description = models.CharField(max_length=200,null = False)
    content = RichTextField(null = False)
    img = models.ImageField(null=False,upload_to='Article/%Y/%m',default=None)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50,null=True)
    active = models.BooleanField(default=False) #active: show status of Article, 1-PUBLISHED, 0-CHECKING

    def __str__(self):
        return self.title

# class Images_Article(models.Model):
#     Article = models.ForeignKey(Article,on_delete = models.CASCADE,null=False,default=None)
#     imgTitle = models.CharField(max_length=100,null=False,default=None)
#     img = models.ImageField(null=False,upload_to='Article/%Y/%m')
#     class Meta:
#         unique_together = (('Article','imgTitle'),)

class Comment(models.Model):
    context = models.TextField(null = False)
    date_posted = models.DateTimeField(auto_now_add=True)
    like_number = models.IntegerField(default=0)    
    dislike_number = models.IntegerField(default=0)
    admin = models.ForeignKey(User,related_name = 'admin_comment',on_delete=models.SET_NULL,null=True)
    commentor = models.ForeignKey(User,related_name = 'commentor_comment',on_delete=models.SET_NULL,null=True)
    Article = models.ForeignKey(Article,on_delete=models.CASCADE,default = None)
    active = models.BooleanField(default=True) #active: show status of comment, 1-ACTIVE, 0-DELETE