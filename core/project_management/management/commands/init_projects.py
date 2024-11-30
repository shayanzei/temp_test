from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.project_management.models import Deadline, Project, Status, Priority, Task
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = "Seed the database with default and test data"

    def get_random_user(self):
        user_ids = User.objects.values_list('id', flat=True)
        if user_ids:
            random_id = random.choice(user_ids)
            return User.objects.get(id=random_id)
        return None

    def handle(self, *args, **kwargs):
        deadline_states = ['Meet', 'extended']
        deadline_instants = []
        for i in range(5):
            deadline_date = datetime.now() + timedelta(days=random.randint(5, 30))
            deadline_instant, created= Deadline.objects.get_or_create(date = deadline_date,
            defaults={'created_by': self.get_random_user(),
                      'state':random.choice(deadline_states)})
            deadline_instants.append(deadline_instant)


        statuses = ['On hold', 'In Progress', 'Completed','Backlog','pending']
        for status_name in statuses:
            Status.objects.get_or_create(name=status_name, defaults={'created_by': self.get_random_user(),})

        priorities = [('Low', 3), ('Medium', 2), ('High', 1)]
        for priority_name, level in priorities:
            Priority.objects.get_or_create(name=priority_name,defaults={'level': level,'created_by': self.get_random_user(),})
        states = ['contracting','planing','designing','development','done']
        for i in range(3):
            project_name = f"Test Project {i + 1}"
            Project.objects.get_or_create(
                name=project_name,
                defaults={
                    'description': f"This is a description for {project_name}",
                    'start_date': datetime.now().date(),
                    'deadline': random.choice(deadline_instants),
                    'created_by': self.get_random_user(),
                    'state': random.choice(states)
                }
            )

        for i in range(10):
            task_title = f"Test Task {i + 1}"
            Task.objects.get_or_create(
                project=Project.objects.order_by('?').first(),
                title=task_title,
                defaults={
                    'description': f"This is a description for {task_title}",
                    'assigned_to': self.get_random_user(),
                    'deadline': random.choice(deadline_instants),
                    'status': Status.objects.order_by('?').first(),
                    'priority': Priority.objects.order_by('?').first(),
                }
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database with test data."))
