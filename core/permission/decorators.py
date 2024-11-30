from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from functools import wraps
from .models import UserRole, RolePermission

def role_required(role_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                try:
                    user_roles = UserRole.objects.filter(user=request.user)
                    for user_role in user_roles:
                        if UserRole.objects.filter(user=request.user ,role__name=role_name).exists():
                            return view_func(request, *args, **kwargs)
                        else:
                            return HttpResponseForbidden("You do not have the required role.")
                except UserRole.DoesNotExist:
                    return HttpResponseForbidden("You do not have any assigned roles.")
            return HttpResponseForbidden("You must be logged in to access this page.")
        return _wrapped_view
    return decorator

def permission_required(permission_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                try:
                    user_roles = UserRole.objects.filter(user=request.user)
                    for user_role in user_roles:
                        if RolePermission.objects.filter(role=user_role.role, permission__name=permission_name).exists():
                            return view_func(request, *args, **kwargs)
                    return HttpResponseForbidden("You do not have the required permission.")
                except UserRole.DoesNotExist:
                    return HttpResponseForbidden("You do not have any assigned roles.")
            return HttpResponseForbidden("You must be logged in to access this page.")
        return _wrapped_view
    return decorator