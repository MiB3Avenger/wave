from rest_framework import serializers
from .models import Post
from .models import Comment
from django.contrib.auth.models import User
from django.utils.timezone import utc
from datetime import datetime
from modules.account.serializers import AccountPhotoSerializer, AccountSerializer
from modules.account.models import Profile

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()

    def get_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
    
    def get_details(self, obj):
        # user = User.objects.filter(id=obj.id)
        profile = Profile.objects.filter(user=obj)
        return AccountPhotoSerializer(profile).data

    class Meta:
        model = User
        fields = ['id', 'username', 'details', 'name', 'first_name', 'last_name']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        user = User.objects.filter(id=obj.author.id)
        return UserSerializer(user, many=True).data[0]

    class Meta:
        model = Comment
        fields = ['id', 'author', 'body', 'post', 'commented_at']

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'body', 'post', 'commented_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    posted_at = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_author(self, obj):
        user = User.objects.filter(id=obj.author.id)
        return UserSerializer(user, many=True).data[0]

    def get_posted_at(self, obj):
        now = datetime.utcnow().replace(tzinfo=utc)
        timediff = now - obj.posted_at

        time = 'just now'

        if (timediff.total_seconds() > 65):
            time = '1 minute ago'

        if (timediff.total_seconds() > 125):
            time = str(int(timediff.total_seconds() // 120)) + ' minutes ago'
        
        if (timediff.total_seconds() // 60 > 65):
            time = '1 hour ago'

        if (timediff.total_seconds() // 60 > 125):
            time = str(int(timediff.total_seconds() // 60 // 60)) + ' hours ago'
        
        if (timediff.total_seconds() // 60 // 60 > 24):
            time = '1 day ago'

        if (timediff.total_seconds() // 60 // 60 > 24):
            time = str(int(timediff.total_seconds() // 60 // 60 // 24)) + ' days ago'

        return time

    def get_comments(self, obj):
        try:
            comments = Comment.objects.filter(post=obj.id)
            return CommentSerializer(comments, many=True).data

        except Comment.DoesNotExist:
            return {}

    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'image', 'likes_count', 'posted_at', 'comments']

class PostPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['image']
        
