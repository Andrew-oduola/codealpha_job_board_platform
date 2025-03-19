from .serializers import JobApplicationSerializer, JobListingSerializer
from rest_framework import viewsets
from .models import JobListing, JobApplication

# Create your views here.
class JobListingViewset(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    
    
class JobApplicationViewset(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    
