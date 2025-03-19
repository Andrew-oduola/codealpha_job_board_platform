from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import EmployerProfile, JobSeekerProfile

User = get_user_model()

class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'is_employer', 'is_job_seeker']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            is_employer=validated_data.get('is_employer', False),
            is_job_seeker=validated_data.get('is_job_seeker', False),
        )
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_employer', 'is_job_seeker']

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_description']

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerProfile
        fields = ['bio', 'skills']