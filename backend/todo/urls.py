from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from todo.views import TodoViewSet

router = DefaultRouter()

router.register('todo', TodoViewSet, basename='Todos')

urlpatterns = [
    path('', include(router.urls))
]
# urlpatterns += router.urls
