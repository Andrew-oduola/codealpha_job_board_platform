import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker


User = get_user_model()

@pytest.mark.django_db
class TestRetriveJobsLists(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testpass')
        self.job_listing = baker.make('jobs.JobListing')
        
    def test_if_unauthenticated_user_returns_joblisting_returns_401(self):
        response = self.api_client.get('/api/jobs/list/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_get_job_listing(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get('/api/jobs/list/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_authenticated_user_can_get_job_listing_detials_detial(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(f'/api/jobs/list/{self.job_listing.id}/')
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_unauthenticated_user_cannot_get_job_listing(self):
        response = self.api_client.get(f'/api/jobs/list/{self.job_listing.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

       
@pytest.mark.django_db
class TestCreateUpdateDeleteJob(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail.com', password='testuserpassword')
        self.superuser = User.objects.create_superuser(email='testsuperuser@gmail.com', password='testsuperuserpassword')
        self.job_listing = baker.make('jobs.JobListing')
        
    def test_if_authenticated_user_can_create_tables(self):
        self.api_client.force_authenticate(user=self.user) 
        response = self.api_client.post('/api/jobs/list/', {
            "employer": 2,
            "title": "Principal Configuration Engineer",
            "description": "Odio temporibus natus ullam magnam voluptate quod.",
            "job_type": "FT",
            "location": "Earum necessitatibus ut iusto eveniet quis pariatur harum.",
            "salary": "Earum quam porro pariatur.",
            "posted_on": "2025-03-19T11:38:31.972614Z",
            "is_active": True
        })
        assert response.status_code == status.HTTP_201_CREATED
        
    def test_if_unauthenticated_user_cannot_create_jobs(self):
        response = self.api_client.post('/api/jobs/list/', {
            "employer": 2,
            "title": "Principal Configuration Engineer",
            "description": "Odio temporibus natus ullam magnam voluptate quod.",
            "job_type": "FT",
            "location": "Earum necessitatibus ut iusto eveniet quis pariatur harum.",
            "salary": "Earum quam porro pariatur.",
            "posted_on": "2025-03-19T11:38:31.972614Z",
            "is_active": True
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_authenticated_user_can_update_jobs(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.put(f'/api/jobs/list/{self.job_listing.id}/', {
            "employer": 2,
            "title": "Principal Configuration Engineer",
            "description": "Odio temporibus natus ullam magnam voluptate quod.",
            "job_type": "FT",
            "location": "Earum necessitatibus ut iusto eveniet quis pariatur harum.",
            "salary": "Earum quam porro pariatur.",
            "posted_on": "2025-03-19T11:38:31.972614Z",
            "is_active": True
        })
        assert response.status_code == status.HTTP_200_OK
        
    def test_if_is_not_authenticated_user_can_not_update_job(self):
        response = self.api_client.put(f'/api/jobs/list/{self.job_listing.id}/', {
            "employer": 2,
            "title": "Principal Configuration Engineer",
            "description": "Odio temporibus natus ullam magnam voluptate quod.",
            "job_type": "FT",
            "location": "Earum necessitatibus ut iusto eveniet quis pariatur harum.",
            "salary": "Earum quam porro pariatur.",
            "posted_on": "2025-03-19T11:38:31.972614Z",
            "is_active": True
        })
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
     

    def test_if_authenticated_user_can_delete_job(self):
        self.api_client.force_authenticate(user=self.superuser)
        response = self.api_client.delete(f'/api/jobs/list/{self.job_listing.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    
    def test_if_is_not_authenticated_user_can_not_delete_tob(self):
        response = self.api_client.delete(f'/api/jobs/list/{self.job_listing.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
        