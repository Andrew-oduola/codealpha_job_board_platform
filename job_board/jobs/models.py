from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

JOB_TYPE = [
    ('RM', 'Remote'),
    ('PT', 'Part-time'),
    ('FT', 'Full-time')
]

# Create your models here.
class JobListing(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_listings')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    job_type = models.CharField(max_length=255, choices=JOB_TYPE)
    
    def __str__(self):
        return self.title

JOB_APPLICATION_STATUS = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected')
]

class JobApplication(models.Model):
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending', choices=JOB_APPLICATION_STATUS)
    resume = models.FileField(upload_to='uploads/', null=True, blank=True)
    
    class Meta:
        unique_together = ('job', 'applicant')
    
    def __str__(self):
        return f"{self.job} - {self.applicant}"
    
    