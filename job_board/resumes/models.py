from django.db import models
from django.contrib.auth import get_user_model

User =  get_user_model()

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    uploaded_on = models.DateTimeField(auto_now_add=True)