from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company
 
#register student only
def register_student(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_student = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your Account created successfully')
            return redirect('login')
        else:
            messages.warning(request, 'Please enter valid information')
            return redirect('register-student')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_student.html', context)
    
#register recruiter only
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your Account created successfully')
            return redirect('login')
        else:
            messages.warning(request, 'Please enter valid information')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_recruiter.html', context)
    
    
#login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Username or Password is incorrect')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
    
#logout user
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('login')