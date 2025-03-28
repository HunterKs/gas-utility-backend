from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings




class CustomUser(AbstractUser):
    user_id = models.CharField(max_length=50, unique=True)
    is_coordinator = models.BooleanField(default=False)  # 0 for User, 1 for Coordinator

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)
    
    USERNAME_FIELD = 'user_id' 
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.username    

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    request_type = models.CharField(max_length=100)  
    description = models.TextField()  
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  
    submitted_at = models.DateTimeField(auto_now_add=True) 
    resolved_at = models.DateTimeField(null=True, blank=True)  

    def __str__(self):
        return f"{self.request_type} - {self.customer.username}"