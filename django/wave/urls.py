
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from wave import views

router = routers.DefaultRouter()




urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('posts/', views.post_list),
    path('posts/<int:id>', views.post_detail),
    path('comments/', views.comment_detail),
    path('comments/<int:id>', views.post_detail),
    
]


