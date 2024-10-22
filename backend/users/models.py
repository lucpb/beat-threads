from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
    
     # Fix related_name conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Use a unique related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Use a unique related_name
        blank=True,
    )
    

class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    def __str__(self):
        return self.name
    

class CustomerProfile(UserProfile):

    def __str__(self):
        return self.name