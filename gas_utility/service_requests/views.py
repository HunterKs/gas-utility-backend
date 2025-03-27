from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import ServiceRequest, CustomUser
from django.contrib.auth.models import User
from .serializers import ServiceRequestSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        user = authenticate(request, user_id=user_id, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect("home")  # Redirect to home page after login
        # else:
        #     return render(request, "login.html", {"error": "Invalid credentials"})
        if user is not None:
            login(request, user)
            return redirect('/api/')  # Redirect to API page or dashboard
        else:
            return HttpResponse("Invalid credentials", status=401)

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('/login/')