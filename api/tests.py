import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


User = get_user_model()

@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def test_user_can_register(client):
    
    data = {
        'username':'john',
        'password':'123456'
    }
    
    response = client.post(reverse('register'), data)
    
    assert response.status_code == 201
    assert User.objects.filter(username='john').exists()
    assert 'password' not in response.data
    
@pytest.mark.django_db
def test_user_can_login(client):
    User.objects.create_user(username='john',password='123456')
    
    data = {
        'username':'john',
        'password':'123456'
    }

    
    response = client.post(reverse('token_obtain_pair'), data)
    
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data
    
    