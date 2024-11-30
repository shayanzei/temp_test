from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_project, name='create_project'),
    path('<int:project_id>/update/', views.update_project, name='update_project'),
    path('<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('<int:project_id>/detail/', views.project_detail, name='project_detail'),
    path('<int:project_id>/tasks/create/', views.create_task, name='create_task'),
    path('dashboard/', views.project_dashboard, name='project_dashboard'),
]
