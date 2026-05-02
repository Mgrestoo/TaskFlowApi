from rest_framework import serializers
from .models import User, Task

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','completed','created_at']
        read_only_fields = ['id','created_at']
        
    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Title cannot be blank")
        if len(value) <= 2:
            raise serializers.ValidationError("Title should be atleast 3 characters")
        if value[0].isdigit():
            raise serializers.ValidationError('Title cannot start with a number')
        return value
    
    def validate_description(self, value):
        value = value.strip()
        if len(value) > 500:
            raise serializers.ValidationError("Description should not exceed 500 characters")
        return value
            
        
            
            
        