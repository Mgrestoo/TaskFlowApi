from django.urls import path
from .views import RegisterApiview, TaskModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TaskModelViewSet, basename='task')

urlpatterns = [
    path('register/', RegisterApiview.as_view(), name='register'),
    
] + router.urls
