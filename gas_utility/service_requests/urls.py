from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet, login_view, logout_view, home_view
# from . import views 

router = DefaultRouter()
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = [
    path('', login_view, name='login'),  # Default route now loads login page
     path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)),  # API endpoints
]