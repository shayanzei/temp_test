from django.core.management.base import BaseCommand
from core.permission.models import Permission, RolePermission, Role, UserRole
from django.contrib.auth.models import User

def make_permissions():
    permissionTitles = ['view_post', 'delete_post', 'make_post', 'edit_post']
    for eachTitle in permissionTitles:
        instance, created = Permission.objects.get_or_create(name=eachTitle)
        if created:
            print(f"Created permission: {eachTitle}")

def make_roles():
    roleTitles = ['Admin', 'Agent', 'TeamMember', 'Customer']
    for eachTitle in roleTitles:
        instance, created = Role.objects.get_or_create(name=eachTitle)
        if created:
            print(f"Created role: {eachTitle}")


def grant_admin_perms():
    perms = Permission.objects.all()
    adminRole = Role.objects.get(name='Admin')
    for perm in perms:
        instance, created = RolePermission.objects.get_or_create(role=adminRole, permission=perm)
        if created:
            print(f"Assigned permission {perm.name} to Admin role")


def grant_agent_perms():
    perms = ['view_post', 'edit_post', 'delete_post']
    agentRole = Role.objects.get(name='Agent')
    for perm in perms:
        thisperm = Permission.objects.get(name=perm)
        instance, created = RolePermission.objects.get_or_create(role=agentRole, permission=thisperm)
        if created:
            print(f"Assigned permission {perm} to Agent role")


def grant_teammember_perms():
    perms = ['view_post']
    teammemberRole = Role.objects.get(name='TeamMember')
    for perm in perms:
        thisperm = Permission.objects.get(name=perm)
        instance, created = RolePermission.objects.get_or_create(role=teammemberRole, permission=thisperm)
        if created:
            print(f"Assigned permission {perm} to TeamMember role")


def grant_customer_perms():
    perms = ['view_post', 'make_post']
    customerRole = Role.objects.get(name='Customer')
    for perm in perms:
        thisperm = Permission.objects.get(name=perm)
        instance, created = RolePermission.objects.get_or_create(role=customerRole, permission=thisperm)
        if created:
            print(f"Assigned permission {perm} to Customer role")

def create_users():
    user1 = User.objects.create_user(username='erfan_admin', password='qwer1234')
    user2 = User.objects.create_user(username='javad_manager', password='qwer1234')
    user3 = User.objects.create_user(username='mamad_naghaash', password='qwer1234')
    user4 = User.objects.create_user(username='rich_kid', password='qwer1234')
    user5 = User.objects.create_user(username='ali_jakesh', password='qwer1234')
    user8 = User.objects.create_user(username='Kaveh_kooni', password='qwer1234')
    role_admin = Role.objects.get(name='Admin')
    role_agent = Role.objects.get(name='Agent')
    role_teammember = Role.objects.get(name='TeamMember')
    role_customer = Role.objects.get(name='Customer')

    UserRole.objects.get_or_create(user=user8, role=role_agent)
    UserRole.objects.get_or_create(user=user1, role=role_admin)
    UserRole.objects.get_or_create(user=user2, role=role_agent)
    UserRole.objects.get_or_create(user=user3, role=role_teammember)
    UserRole.objects.get_or_create(user=user4, role=role_customer)
    UserRole.objects.get_or_create(user=user5, role=role_agent)
    UserRole.objects.get_or_create(user=user5, role=role_teammember)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        make_permissions()
        make_roles()
        grant_admin_perms()
        grant_agent_perms()
        grant_teammember_perms()
        grant_customer_perms()
        
        create_users()
        
        print("Initialization complete!")
