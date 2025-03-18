from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class JobListing(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class JobApplication(models.Model):
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')