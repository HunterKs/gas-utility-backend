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
from .forms import ServiceRequestForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


class ServiceRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing service requests.
    - Customers can submit service requests.
    - Admins can view, update, or delete requests.
    """
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  
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
            return redirect("home")  
        else:
            error_message = "Invalid User ID or Password"

    return render(request, "login.html", {"error": error_message})

def logout_view(request):
    """Logs out the user and redirects to login page."""
    logout(request)
    return redirect(reverse('login'))  

@login_required
def home_view(request):
    """
    Home page for users and coordinators with service request form.
    """
    form = ServiceRequestForm()
    user = request.user

    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        
       
        if form.is_valid():
            service_request = form.save(commit=False)

            if not user.is_authenticated:
                return render(request, "home.html", {
                    "form": form, 
                    "error": "User is not authenticated"
                })

            service_request.customer = user  
            service_request.status = "Pending"  

            try:
                service_request.save()
                return redirect("home")  
            except IntegrityError as e:
                return render(request, "home.html", {
                    "form": form, 
                    "error": f"Database integrity error: {e}"
                })
        else:
           
            return render(request, "home.html", {
                "form": form, 
                "error": f"Form is not valid: {form.errors}"
            })

    
    if user.is_coordinator:
        service_requests = ServiceRequest.objects.all()[:10]  
    else:
        service_requests = ServiceRequest.objects.filter(customer=user)[:5]  

    return render(request, "home.html", {
        "form": form,
        "service_requests": service_requests,
        "is_coordinator": user.is_coordinator,
    })
        


@login_required
def update_request_status(request, request_id):
    """
    Allows coordinators to update the status of a service request.
    """
    if not request.user.is_coordinator:
        return HttpResponseForbidden("You do not have permission to update statuses.")

    service_request = get_object_or_404(ServiceRequest, id=request_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["Pending", "In Progress", "Resolved"]:
            service_request.status = new_status
            service_request.save()

    return redirect("home")   