from django.urls import path

#post功能，用于测试search
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]


#查找功能
path('search/', views.post_search, name='post_search'),