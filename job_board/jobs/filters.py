import django_filters
from .models import JobListing, JobApplication

class JobListingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive title search
    location = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive location search
    company_name = django_filters.CharFilter(lookup_expr='icontains')  # Assuming there is a company_name field
    salary_min = django_filters.NumberFilter(field_name="salary", lookup_expr="gte")  # Min salary
    salary_max = django_filters.NumberFilter(field_name="salary", lookup_expr="lte")  # Max salary

    class Meta:
        model = JobListing
        fields = ['title', 'location', 'company_name', 'salary']  # Customize based on your model fields



class JobApplicationFilter(django_filters.FilterSet):
    job = django_filters.CharFilter(field_name="job__title", lookup_expr='icontains')  # Filter by job title
    applicant = django_filters.CharFilter(field_name="applicant", lookup_expr='icontains')  # Filter by applicant's name
    status = django_filters.ChoiceFilter(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])  # Adjust status choices as needed
    applied_after = django_filters.DateFilter(field_name="applied_on", lookup_expr='gte')  # Filter by applications after a date
    applied_before = django_filters.DateFilter(field_name="applied_on", lookup_expr='lte')  # Filter by applications before a date

    class Meta:
        model = JobApplication
        fields = ['job', 'applicant', 'status', 'applied_on']