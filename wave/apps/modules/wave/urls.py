
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views
from modules.account import views as accountViews
from rest_framework.authtoken import views as authViews
from modules.account import urls as account
from django.views.static import serve

router = routers.DefaultRouter()

app_name = 'modules.wave'
urlpatterns = [
    path('posts/', views.post_list),
    path('posts/create/<int:id>', views.post_pic_put),
    path('posts/<int:id>', views.post_detail),
    path('posts/<int:id>/comments/', views.comment_list),
    path('comments/', views.comment_detail),
    path('comments/<int:id>', views.post_detail),
    path('posts/<int:id>/like',views.like_detail),

    path('login/', views.login),
    path('register/', views.register),
    path('user/', views.user),
    path('user/<int:id>', views.userById),
    path('user/<str:id>', views.userByUsername),

    path('search/user/', views.searchUsername),

    path('check-token/<str:token>', views.checkToken),

    path('logout/', views.logout),


    path('profile/picture/', accountViews.upload_profile_pic),
    path('profile/details/', accountViews.change_details),

]


