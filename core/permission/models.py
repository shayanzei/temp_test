from django.db import models
from django.contrib.auth.models import User

class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete= models.CASCADE, blank=True, default='')
    permission = models.ForeignKey(Permission, on_delete= models.CASCADE, blank=True, default='')

    class Meta:
        unique_together = ('role', 'permission')

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, default='')
    role = models.ForeignKey(Role, on_delete= models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'role')