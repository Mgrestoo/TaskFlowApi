
from .models import User, Task
from .serializers import RegisterSerializer,TaskSerializer
from rest_framework.generics import CreateAPIView
# from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class RegisterApiview(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  
    
    
class CustomPagination(PageNumberPagination):
    page_query_param = 'p' 
    page_size = 10
    max_page_size = 100
       
class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['completed']
    search_fields = ['title','description']
    ordering_fields = ['created_at']
    
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
     
