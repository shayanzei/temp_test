
from django.test import TestCase
from .forms import ProjectForm, TaskForm
from datetime import date

class ProjectFormTests(TestCase):

    def test_valid_project_form(self):
        form_data = {
            'name': 'New Project',
            'state': 'Draft',
            'description': 'A new project description',
            'start_date': date(2024, 12, 1), 
            'due_date': date(2024, 12, 31)  
        }
        form = ProjectForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_project_form(self):
        form_data = {
            'name': '',
            'start_date': date(2024, 12, 1),
            'due_date': date(2024, 11, 30)
        }
        form = ProjectForm(data=form_data)
        self.assertFalse(form.is_valid())


class TaskFormTests(TestCase):

    def test_valid_task_form(self):
        form_data = {
            'title': 'New Task',
            'due_date': date(2024, 12, 25)
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_task_form(self):
        form_data = {
            'title': '',
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

