from django.db import models
from users.models import User


class Resume(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    job_title = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    
    
