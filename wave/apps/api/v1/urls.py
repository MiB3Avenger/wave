from django.urls import path, include

from .views import (
    index,
)

app_name = 'api.v1'
urlpatterns = [
    path('', index, name="default"),
    path('', include('modules.wave.urls', namespace='modules.wave'))
]
