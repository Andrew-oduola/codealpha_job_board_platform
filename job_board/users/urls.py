from django.urls import path
from .views import EmployerRegistrationView, JobSeekerRegistrationView

urlpatterns = [
    path('register/employer/', EmployerRegistrationView.as_view(), name='employer_register'),
    path('register/jobseeker/', JobSeekerRegistrationView.as_view(), name='jobseeker_register'),
]