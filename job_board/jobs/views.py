from .serializers import JobApplicationSerializer, JobListingSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import JobListing, JobApplication
from .filters import JobListingFilter, JobApplicationFilter


# Create your views here.
class JobListingViewset(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = JobListingFilter               
    search_fields = ['title', 'company_name', 'location']  # Enable search
    ordering_fields = ['salary', 'created_at']  # Sorting by salary and creation date
    permission_classes = [IsAuthenticated]
           
    
    
class JobApplicationViewset(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = JobApplicationFilter
    search_fields = ['job__title', 'applicant__name']  # Enable search by job title and applicant name
    ordering_fields = ['applied_at', 'status']  # Sorting by application date and status
    permission_classes = [IsAuthenticated]

    
    
