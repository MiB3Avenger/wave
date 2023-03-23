
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from wave import views
from account import views as accountViews
from rest_framework.authtoken import views as authViews
from account import urls as account
from django.views.static import serve

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/account/', include(account.urlpatterns)),

    path('api/posts/', views.post_list),
    path('api/posts/create/<int:id>', views.post_pic_put),
    path('api/posts/<int:id>', views.post_detail),
    path('api/posts/<int:id>/comments/', views.comment_list),
    path('api/comments/', views.comment_detail),
    path('api/comments/<int:id>', views.post_detail),
    path('api/posts/<int:id>/like',views.like_detail),

    path('api/login/', views.login),
    path('api/register/', views.register),
    path('api/user/', views.user),
    path('api/user/<int:id>', views.userById),
    path('api/user/<str:id>', views.userByUsername),

    path('api/search/user/', views.searchUsername),

    path('api/check-token/<str:token>', views.checkToken),

    path('api/logout/', views.logout),


    path('api/profile/picture/', accountViews.upload_profile_pic),
    path('api/profile/details/', accountViews.change_details),

    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),
    re_path(r'^.*$', views.home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


