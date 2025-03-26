from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet

router = DefaultRouter()
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),  # API base path
]
