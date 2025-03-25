import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker


User = get_user_model()

@pytest.mark.django_db
class TestRetriveJobApplication(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.job_application = baker.make('jobs.JobApplication')
        
    def test_if_unauthenticated_user_returns_job_application_returns_401(self):
        response = self.api_client.get('/api/jobs/application/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_get_job_applications(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/jobs/application/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_authenticated_user_can_get_job_application_detial(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(f'/api/jobs/application/{self.job_application.id}/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_unauthenticated_user_cannot_get_job_applications(self):
        response = self.api_client.get(f'/api/jobs/application/{self.job_application.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
