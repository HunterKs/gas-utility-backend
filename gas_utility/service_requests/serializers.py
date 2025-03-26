from rest_framework import serializers
from .models import ServiceRequest

class ServiceRequestSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')  # Show customer username

    class Meta:
        model = ServiceRequest
        fields = '__all__'  # Include all model fields
