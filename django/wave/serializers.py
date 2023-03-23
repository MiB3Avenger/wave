from rest_framework import serializers
from .models import Post
from .models import Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'comment', 'post', 'commented_at']

class PostSerializer(serializers.ModelSerializer):
    # likes = UserSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'image', 'likes_count']

class PostPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['image']
        
