from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


#将blog下的urls包含在大项目中
urlpatterns = [
    path('admin/', admin.site.urls),
    #blog的post，用于测试search
    path('blog/', include('blog.urls', namespace='blog')),
    #用户账号
    path('account/', include('account.urls')),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)