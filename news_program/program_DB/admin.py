from django.contrib import admin
from .models import News,Categories
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['name']

class NewsAdmin(admin.ModelAdmin):
    search_fields = ['name']

class NewsForm(forms.Form):
    content = forms.CharField(widgets = CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = '__all__'  

admin.site.register(News,NewsAdmin)
admin.site.register(Categories,CategoriesAdmin)


