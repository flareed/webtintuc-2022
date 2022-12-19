from django.contrib import admin
from .models import Article,Category,User,Subscriber
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import Permission
# Register your models here.

class ArticleInLine(admin.StackedInline):
    model = Article
    pk_name = 'category'

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget = CKEditorUploadingWidget)

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title','date_posted','active']
    ordering = ['date_posted']
    form = ArticleForm

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    #inlines = (ArticleInLine, )


class ArticleProgramAdminSite(admin.AdminSite):
    site_header = 'THE23POST'

#class SubscriberAdmin(admin.ModelAdmin)


# admin_site = ArticleProgramAdminSite('myProgram')

# admin_site.register(Article,ArticleAdmin)
# admin_site.register(Category,CategoryAdmin)
# admin_site.register(User)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(Subscriber)



