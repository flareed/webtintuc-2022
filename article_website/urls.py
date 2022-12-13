"""article_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "Article API"
        default_version= 'v1',
        description= "APIs for Article Website",
        contact= openapi.Contact(email = "the23post@gmail.com"),
        license= openapi.License(name = "The 23 Post"),
    ),
    public = True,
    permisson_classes=(permissions.AllowAny,),


)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('myApp.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('o/',include('oauth2_provider.urls',
         namespace ='oauth2_provider')),
    re_path(r'^ckeditor/',include('ckeditor_uploader.urls')),
]
