from django.urls import path, include
from rest_framework import routers
from .views import JobListingViewset, JobApplicationViewset

router = routers.DefaultRouter()
router.register('list', JobListingViewset)
router.register('application', JobApplicationViewset)


urlpatterns = [
    path('', include(router.urls))
]
