from rest_framework import serializers
from .models import JobListing, JobApplication

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['id', 'employer', 'title', 'description', 'location', 'salary', 'posted_on', 'is_active']
        
        
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'job', 'applicant', 'applied_on', 'status']
        
