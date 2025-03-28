from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet, login_view, logout_view, home_view, update_request_status
# from . import views 

router = DefaultRouter()
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = [
    path('', login_view, name='login'), 
     path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)),  
    path('update-request-status/<int:request_id>/', update_request_status, name='update_request_status'),
]