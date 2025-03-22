from django.contrib import admin
from .models import JobListing, JobApplication

# Register your models here.
@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    pass

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    pass

