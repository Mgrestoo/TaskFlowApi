from django.urls import path
from .views import RegisterApiview


urlpatterns = [
    path('register/', RegisterApiview.as_view(), name='get-token'),
    
]
