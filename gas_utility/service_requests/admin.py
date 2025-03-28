from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ServiceRequest, CustomUser

@admin.register(ServiceRequest)

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'request_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('customer__username', 'request_type')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('user_id', 'username', 'is_coordinator', 'is_staff', 'is_active')
    search_fields = ('user_id', 'username')
    list_filter = ('is_coordinator', 'is_staff', 'is_active')

    fieldsets = (
        ('User Information', {'fields': ('user_id', 'username', 'password')}),
        ('Permissions', {'fields': ('is_coordinator', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        ('Create New User', {
            'classes': ('wide',),
            'fields': ('user_id', 'username', 'password1', 'password2', 'is_coordinator', 'is_staff', 'is_active')}
        ),
    )

    ordering = ('user_id',)  

admin.site.register(CustomUser, CustomUserAdmin)
