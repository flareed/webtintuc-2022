from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users',views.UserViewSet)
router.register('categories',views.CategoryViewSet)
router.register('articles',views.ArticleViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
