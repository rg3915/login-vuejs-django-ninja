from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from .api import api


def about(request):
    return JsonResponse({'status': 'OK'})


urlpatterns = [
    path('about/', about),
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]
