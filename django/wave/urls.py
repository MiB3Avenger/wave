
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from wave import views
from rest_framework.authtoken import views as authViews
from account import urls as account

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/account/', include(account.urlpatterns)),
    path('api/posts/', views.post_list),
    path('api/posts/<int:id>', views.post_detail),
    path('api/comments/', views.comment_detail),
    path('api/comments/<int:id>', views.post_detail),
    path('api/posts/<int:id>/like',views.like_detail),
    path('api/login/', views.login),
    path('api/register/', views.register),
    path('api/user/', views.user),
    path('api/user/<int:id>', views.userById),
    path('api/user/<str:id>', views.userByUsername),
    path('api/check-token/<str:token>', views.checkToken),
    path('api/logout/', views.logout),
    re_path(r'^.*$', views.home),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


