from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Links request to a user
    request_type = models.CharField(max_length=100)  # Type of request (e.g., gas leak, billing issue)
    description = models.TextField()  # Detailed description of the request
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # File upload (optional)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Request status
    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp when request was submitted
    resolved_at = models.DateTimeField(null=True, blank=True)  # Timestamp when request was resolved

    def __str__(self):
        return f"{self.request_type} - {self.customer.username}"
