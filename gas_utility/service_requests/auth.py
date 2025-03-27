from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def authenticate_user(request):
    """Authenticate user using user_id instead of username."""
    user_id = request.POST.get("user_id")  # Use user_id, not username
    password = request.POST.get("password")

    try:
        user = CustomUser.objects.get(user_id=user_id)  # Ensure user_id exists
        authenticated_user = authenticate(request, username=user.username, password=password)
        return authenticated_user
    except CustomUser.DoesNotExist:
        return None

def login_user(request, user):
    """Logs in the user."""
    login(request, user)

def logout_user(request):
    """Logs out the user."""
    logout(request)
