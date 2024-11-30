from django.contrib import admin
from .models import Permission,RolePermission,Role,UserRole
admin.site.register(RolePermission)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(UserRole)