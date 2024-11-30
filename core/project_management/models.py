from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Deadline(models.Model):
    date = models.DateTimeField(null=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='deadlines')
    
    def clean(self):
        if self.date < now().date():
            raise ValidationError("Due date cannot be in the past.")

class Project(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_projects')

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.due_date is not None and self.due_date < now().date():
            raise ValidationError("Start date cannot be in the past.")

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='statuses')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "status"
        verbose_name_plural = "statuses"

class Priority(models.Model):
    name = models.CharField(max_length=50, unique=True)
    level = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='priorities')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "priority"
        verbose_name_plural = "priorities"
        unique_together = ('name', 'level')

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks')
    
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks')
        
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks')
    
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks')

    def __str__(self):
        return f"{self.title} ({self.project.name})" 
    def clean(self):
        if self.due_date is not None and self.due_date < now().date():
            raise ValidationError("Start date cannot be in the past.")   

class HistoryLog(models.Model):
    action = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    changes = models.JSONField(blank=True, null=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='history_logs')
    
    content_type = models.ForeignKey(
        ContentType,
        null=True, blank=True,
        on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.action} by {self.user} on {self.model} ({self.object_id})"
