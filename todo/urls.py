from django.urls import path, include
from rest_framework import routers
from todo.views import CategoryViewSet, TodoViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('category', CategoryViewSet, basename='category_api')
router.register('todo', TodoViewSet, basename='todo_api')

urlpatterns = [
    path('', include(router.urls)),

]
