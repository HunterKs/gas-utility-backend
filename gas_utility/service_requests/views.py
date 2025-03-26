from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

class ServiceRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing service requests.
    - Customers can submit service requests.
    - Admins can view, update, or delete requests.
    """
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can create/update requests

    def perform_create(self, serializer):
        """
        Assign the logged-in user as the customer when creating a request.
        """
        serializer.save(customer=self.request.user)
