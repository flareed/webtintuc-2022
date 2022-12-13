from rest_framework.serializers import ModelSerializer
from .models import Category,User,Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ["author","title","content","date_posted","active"]

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
    articles = ArticleSerializer(Article,many=True)
    class Meta:
        model = Category
        fields = ["id","name","description","articles"]