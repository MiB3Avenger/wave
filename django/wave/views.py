from django.shortcuts import render
from .models import Post, Comment
from django.http import JsonResponse
from .serializers import PostSerializer, CommentSerializer, PostInputSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import base64 
from django.core.files.base import ContentFile

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    
    if request.method == 'GET':
        posts = Post.objects.filter(user_deleted=False,admin_deleted=False)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        image_data = request.data['image']
        format, imgstr = image_data.split(';base64,')
        print("format", format)
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))  
        file_name = "'myphoto." + ext
        post = PostSerializer()  
        post.body = request.data['body']
        post.author = request.user
        if post.is_valid():
            post.save()
            post.image.save(file_name, data)
            return Response(post, status=status.HTTP_201_CREATED)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_detail(request,id):
    try:
       post = Post.objects.get(pk=id,user_deleted=False,admin_deleted=False)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
     
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.user_deleted=True
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list(request):
    
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request,id):
    try:
       comment = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
     
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def like_detail(request,id):
    try:
       post = Post.objects.get(pk=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
     
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        post.likes_count+=1
        post.likes.add(request.user)
        post.save()
        return Response(status=status.HTTP_200_OK)
        
    
    elif request.method == 'DELETE':
        post.likes-=1
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def image_detail(request,id):
#     try:
#        post = Post.objects.get(pk=id,image=True)
#     except Comment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)   
     
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         post.likes_count+=1
#         post.likes.add(request.user)
#         post.save()
#         return Response(status=status.HTTP_200_OK)
        
    
#     elif request.method == 'DELETE':
#         post.likes-=1
#         return Response(status=status.HTTP_204_NO_CONTENT)