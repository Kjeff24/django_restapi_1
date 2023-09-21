from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# User models that includes employee and employers
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars/')
    phone_number = models.CharField(unique=True, null=True,blank=True, max_length=25)
    date_joined = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"