from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    path('admin', RedirectView.as_view(url='admin/', permanent=False)),
    path('admin/', admin.site.urls, name='admin'),

    # List all api paths
    path('api/v1/', include('api.v1.urls')),
]

if getattr(settings, "DEBUG", False):
    import debug_toolbar
    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
