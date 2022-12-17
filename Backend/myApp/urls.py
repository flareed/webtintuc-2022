from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('users',views.UserViewSet,'user')
router.register('categories',views.CategoryViewSet,'category')
router.register('articles',views.ArticleViewSet,'article')
router.register('subscribers',views.SubscriberViewSet,'subscriber')

urlpatterns = [
    path('',include(router.urls)),
]


