from rest_framework import generics, permissions
from .serializers import CustomUserCreateSerializer, EmployerProfileSerializer, JobSeekerProfileSerializer
from .models import EmployerProfile, JobSeekerProfile

class EmployerRegistrationView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_employer=True)
        EmployerProfile.objects.create(user=user)

class JobSeekerRegistrationView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_job_seeker=True)
        JobSeekerProfile.objects.create(user=user)