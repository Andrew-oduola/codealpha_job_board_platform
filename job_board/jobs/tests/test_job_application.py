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
        

@pytest.mark.django_db
class TestCreateUpdateDeleteJobApplication(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testuserpassword')
        self.superuser = User.objects.create_superuser(email='testsuperuser@gmail.com', password='testsuperuserpassword')
        self.job_application = baker.make('jobs.JobApplication')
        
    def test_if_authenticated_user_can_create_job_application(self):
        self.api_client.force_authenticate(user=self.user) 
        response = self.api_client.post('/api/jobs/application/', {
            "job": 1,
            "applicant": 1,
            "applied_on": "2025-03-22T13:42:40.625601Z",
            "status": "pending"
            })
        assert response.status_code == status.HTTP_201_CREATED
        
        
    def test_if_unauthenticated_user_cannot_create_jobs_application(self):
        response = self.api_client.post('/api/jobs/application/', {
            "job": 1,
            "applicant": 1,
            "applied_on": "2025-03-22T13:42:40.625601Z",
            "status": "pending"
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_update_job_application(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.put(f'/api/jobs/application/{self.job_application.id}/', {
            "job": 1,
            "applicant": 1,
            "applied_on": "2025-03-22T13:42:40.625601Z",
            "status": "pending"
            })
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_is_not_authenticated_user_can_not_update_job_application(self):
        response = self.api_client.put(f'/api/jobs/list/{self.job_application.id}/', {
            "job": 1,
            "applicant": 1,
            "applied_on": "2025-03-22T13:42:40.625601Z",
            "status": "pending"
            })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
     

    def test_if_authenticated_user_can_delete_job(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.delete(f'/api/jobs/application/{self.job_application.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    
    def test_if_is_not_authenticated_user_can_not_delete_tob(self):
        response = self.api_client.delete(f'/api/jobs/application/{self.job_application.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
        