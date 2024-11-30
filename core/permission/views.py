from .decorators import role_required,permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from.models import RolePermission


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'Username: {username}, Password: {password}')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            messages.error(request, 'Invalid credentials')
    else:
            messages.error(request, 'Please enter both username and password')
    return render(request, 'login.html')
    
@csrf_exempt   
@role_required('Admin')
def dashboard(request):
    edit_post_feature = 'you can edit posts'
    context = {
    'edit_post_feature': edit_post_feature
    }
    
    return render(request, 'dashboard.html', context)
  
