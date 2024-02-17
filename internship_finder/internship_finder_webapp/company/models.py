from django.db import models
from users.models import User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    est_date = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state= models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name
