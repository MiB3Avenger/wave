from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from .serializers import AccountSerializer, AccountPhotoSerializer, AccountDetailsSerializer
from django.contrib.auth.models import User, auth
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

import json

#login
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})



def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'账户 {username} 创建成功！请登录。')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


#register
def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

#search users
def search_user(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        users = User.objects.filter(username__icontains=search_term)
        return render(request, 'account/search_user.html', {'users': users, 'search_term': search_term})
    else:
        return render(request, 'account/search_user.html')


@login_required
def edit(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@api_view(['PUT'])
@authentication_classes([])
@parser_classes([MultiPartParser])
def upload_profile_pic(request):
    user = auth.get_user(request)
    profile, created = Profile.objects.get_or_create(user=user)

    picture = AccountPhotoSerializer(profile, data=request.data)
    if picture.is_valid():
        picture.save()
        return Response(picture.data)
    
    return Response(json.dumps(request.data['photo']))

@api_view(['POST'])
@authentication_classes([])
def change_details(request):
    user = auth.get_user(request)
    userObject = User.objects.get(id=user.id)

    userAuth = auth.authenticate(username=user.username, password=request.data['password'])
    if(userAuth is not None):

        data = {'username': request.data['username'], 'email': request.data['email']}
        userSerializer = AccountDetailsSerializer(userObject, data=data)
        
        if(userSerializer.is_valid()):
            userSerializer.save()
            return Response(userSerializer.data)
    
    return Response({'success':False},status=status.HTTP_400_BAD_REQUEST)