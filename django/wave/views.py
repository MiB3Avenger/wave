from django.shortcuts import render
from .models import Post, Comment
from django.http import JsonResponse
from .serializers import PostPicSerializer, PostSerializer, CommentSerializer
from django.contrib.auth.models import User, auth
from django.core import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser

from account.models import Profile
from account.serializers import AccountSerializer

def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def checkToken(request,token):
    # is_tokened = Token.objects.filter(user=request.user,key=token).exist()
    user=auth.get_user(request)
    
    return Response({'user':user.username})

@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    try:
        if(username == "" or password == ""):
            return Response({'success': False, 'message': 'Please enter your credentials.'}, status=status.HTTP_400_BAD_REQUEST)

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'username': user.username,
                'name': user.first_name + " " + user.last_name
            })
        else:
            return Response({'success': False, 'message': 'Invalid Credentials.'}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    username = request.data['username']
    email = request.data['email']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    password = request.data['password']
    confirm_password = request.data['password_confirm']

    try:
        if(username == ""
           or email == ""
           or first_name == ""
           or last_name == ""
           or password == ""
           or confirm_password == ""
        ):
            return Response({'success': False, 'message': 'Please enter your details.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if(password != confirm_password):
            return Response({'success': False, 'message': 'Password and confirm passwords are not same.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            getUsername = User.objects.get(username=username)
            if(getUsername is not None):
                return Response({'success': False, 'message': 'Username already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        try:
            getUserEmail = User.objects.get(email=email)
            if(getUserEmail is not None):
                return Response({'success': False, 'message': 'Email already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=True
        )

        auth.login(request,user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'name': user.first_name + " " + user.last_name
        })
        # return Response({'success': True})

    except:
        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([])
def user(request):
    user = auth.get_user(request)

    response = {
        'username': user.username,
        'email': user.email,
        'name': user.first_name + " " + user.last_name,
        'id': user.id,
        'auth_user': True
    }

    try:
        profile = Profile.objects.filter(user=user.id)
        profileSerialized = AccountSerializer(profile, many=True)
        response['profile'] = profileSerialized.data[0]

        posts = Post.objects.filter(author=user.id)

        postsSerialized = PostSerializer(posts, many=True)
        response['posts'] = postsSerialized.data
    
        return Response(response)
    except:
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([])
def userById(request,id):
    user=User.objects.get(id=id)
    auth_user = auth.get_user(request)

    response = {
        'username': user.username,
        'email': user.email,
        'name': user.first_name + " " + user.last_name,
        'id': user.id,
        'auth_user': user.id == auth_user.id
    }

    try:
        posts = Post.objects.filter(author=user.id)

        postsSerialized = PostSerializer(posts, many=True)
        response['posts'] = postsSerialized.data
    
        return Response(response)
    except:
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([])
def userByUsername(request,id):
    user=User.objects.get(username=id)
    auth_user = auth.get_user(request)

    response = {
        'username': user.username,
        'email': user.email,
        'name': user.first_name + " " + user.last_name,
        'id': user.id,
        'auth_user': user.id == auth_user.id
    }

    try:
        posts = Post.objects.filter(author=user.id)

        postsSerialized = PostSerializer(posts, many=True)
        response['posts'] = postsSerialized.data
    
        return Response(response)
    except:
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([])
def logout(request):
    # user=auth.get_user(request)
    # request.user
    auth.logout(request)
    return Response({'success': True})


@api_view(['GET'])
def searchUsername(request):
    string = request.GET['search']
    if(string == ''):
        return Response({'success': False, 'message': 'Enter something to search users.'})

    users = User.objects.filter(username__icontains=string)[:10]

    serialized_queryset = serializers.serialize('json', users)
    return Response({'success':True,'users': users.values()})


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(user_deleted=False,admin_deleted=False)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        post = Post.objects.create(
            author_id = request.data['author_id'],
            body = request.data['body']
        )
        return Response({'post': post.id})

@api_view(['PUT'])
@authentication_classes([])
@parser_classes([MultiPartParser])
def post_pic_put(request,id):
    try:
       post = Post.objects.get(pk=id,user_deleted=False,admin_deleted=False)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    serializer = PostPicSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
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
@authentication_classes([])
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
@authentication_classes([])
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
@authentication_classes([])
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


