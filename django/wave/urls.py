
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from wave import views
from rest_framework.authtoken import views as authViews

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('account/', account.site.urls),
=======
    path('posts/', views.post_list),
    path('posts/<int:id>', views.post_detail),
    path('comments/', views.comment_detail),
    path('comments/<int:id>', views.post_detail),
    path('posts/<int:id>/like',views.like_detail),
    path('login/', authViews.obtain_auth_token)
>>>>>>> main
]


