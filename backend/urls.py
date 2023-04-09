from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from .api import api


def todo(request):
    data = [
        {
            "id": 1,
            "task": "The quick brown fox"
        },
        {
            "id": 2,
            "task": "over the lazy dog"
        }
    ]
    return JsonResponse(data, safe=False)


def about(request):
    return JsonResponse({'status': 'OK'})


urlpatterns = [
    path('todo/', todo),
    path('about/', about),
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]
