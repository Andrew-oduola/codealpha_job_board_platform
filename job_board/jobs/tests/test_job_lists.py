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
