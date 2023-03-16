from rest_framework import serializers
from .models import Post
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'comment', 'post', 'commented_at' ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'posted_at', 'likes', 'likes_count']
        
