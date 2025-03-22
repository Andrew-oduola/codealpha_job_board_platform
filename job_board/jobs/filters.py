import django_filters
from .models import JobListing

class JobListingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive title search
    location = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive location search
    company_name = django_filters.CharFilter(lookup_expr='icontains')  # Assuming there is a company_name field
    salary_min = django_filters.NumberFilter(field_name="salary", lookup_expr="gte")  # Min salary
    salary_max = django_filters.NumberFilter(field_name="salary", lookup_expr="lte")  # Max salary

    class Meta:
        model = JobListing
        fields = ['title', 'location', 'company_name', 'salary']  # Customize based on your model fields
