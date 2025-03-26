from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'request_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('customer__username', 'request_type')

