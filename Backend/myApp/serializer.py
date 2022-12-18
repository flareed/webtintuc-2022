from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Category,User,Article,Subscriber
from rest_framework import serializers


    

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password","avatar"]

        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user

    

class CategorySerializer(ModelSerializer):
    #articles = ArticleSerializer(Article,many=True)
    class Meta:
        model = Category
        fields = ["id","name","description"]


class ArticleSerializer(ModelSerializer):
    # image = SerializerMethodField()

    # def get_image(self,Article):
    #     request = self.context['request']
    #     name = Article.img.name
    #     if name.startswith("static/"):
    #         path = '/%s' % name
    #     else:
    #         path = '/static/%s' % name
        
    #     return request.build_absolute_uri(path)
    
    category = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = ["id","category","author","title","description","content","location","date_posted","img"]


class SubscriberSerializer(ModelSerializer):
    categories = serializers.StringRelatedField(many = True)
    class Meta:
        model = Subscriber
        fields = ["id","subscriber","categories"]
