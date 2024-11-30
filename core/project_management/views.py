from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Task, Project
from .forms import TaskForm, ProjectForm
from core.utils.form_helpers import handle_form
from core.utils.soft_delete_helper import handle_soft_delete

def create_project(request):
        return handle_form(
        request,
        form_class=ProjectForm,
        template_name='project_form.html',
        success_url_name='project_detail'
    )

def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return handle_form(
        request,
        form_class=ProjectForm,
        template_name='project_form.html',
        instance=project,
        success_url_name='project_detail'
    )


def delete_project(request, project_id):
    return handle_soft_delete(
        request,
        model_class=Project,
        object_id=project_id,
        success_url_name='projects_dashboard'
    )   

def create_task(request, project_id):
    return handle_form(
        request,
        form_class=TaskForm,
        template_name='task_form.html',
        success_url_name='project_detail',
        extra_context={'project_id': project_id}
    )

def update_task(request, task_id):
   task = get_object_or_404(Task, id=task_id)
   return handle_form(
       request,
       form_class=TaskForm,
       template_name='task_form.html',
       instance=task,
       success_url_name='task_detail'
   )

def delete_task(request, task_id):
    return handle_soft_delete(
        request,
        model_class=Task,
        object_id=task_id,
        success_url_name='tasks_dashboard'
    )

def project_dashboard(request):
     projects = Project.objects.filter(is_deleted=False)
     return render(
          request, 'project_dashboard.html',
          {'projects': projects})

def project_detail(request, project_id):
     project = get_object_or_404(Project, id=project_id)
     tasks = project.tasks.filter(is_deleted=False)
     return render(
          request, 'project_detail.html', 
          {'project': project, 'tasks': tasks})