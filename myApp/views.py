
from rest_framework import viewsets,generics, permissions,status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import render
from .models import *
from .serializer import UserSerializer,CategorySerializer,ArticleSerializer



class UserViewSet(viewsets.ViewSet,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView,
                  generics.UpdateAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(active = True)
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class ArticleViewSet(viewsets.ModelViewSet):   
    queryset = Article.objects.filter(active = True)
    serializer_class = ArticleSerializer

    @action(methods=['post'],detail=True)
    #/article/{pk}/active_article
    def active_article(self,request,pk):
        try:
            a = Article.objects.get(pk = pk)
            a.active = True
            a.save()
        except Article.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(ArticleSerializer(a).data,status = status.HTTP_200_OK)

    @action(methods=['post'],detail=True)
    #/article/{pk}/hide_article
    def hide_article(self,request,pk):
        try:
            a = Article.objects.get(pk = pk)
            a.active = False
            a.save()
        except Article.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(ArticleSerializer(a).data,status = status.HTTP_200_OK)





    
