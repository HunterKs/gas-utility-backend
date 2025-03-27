from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.urls import reverse
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from .auth import authenticate_user, login_user, logout_user
from django.contrib.auth.decorators import login_required


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

def login_view(request):
    """
    Custom login view for handling user authentication.
    """
    
    error_message = None
    if request.method == "POST":
        user = authenticate_user(request)

        if user is not None:
            login(request, user)
            return redirect("home")  # Change this to the actual view name
        else:
            error_message = "Invalid User ID or Password"

    return render(request, "login.html", {"error": error_message})

def logout_view(request):
    """Logs out the user and redirects to login page."""
    logout(request)
    return redirect(reverse('login'))  # Use reverse() for flexibility

@login_required
def home_view(request):
    """
    Home page view for authenticated users.
    """
    return render(request, "home.html") 
