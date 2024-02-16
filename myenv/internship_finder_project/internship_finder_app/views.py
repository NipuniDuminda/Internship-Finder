from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from . forms import CreateUserForm,LoginForm

#Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout

def homepage(request):
     template = loader.get_template('homepage.html')
     return HttpResponse(template.render())

def register(request):
     form = CreateUserForm()

     if request.method=="POST":
          form=CreateUserForm(request.POST)

          if form.is_valid():
               form.save()
               return redirect('login')

     context ={'registerform':form}
     return render(request,'register.html',context=context)

def login(request):

     form = LoginForm()

     if request.method == 'POST':
          form = LoginForm(request,data=request.POST)

          if form.is_valid():
               username=request.POST.get('username')
               password=request.POST.get('password')

               user = authenticate(request,username=username,password=password)

               if user is not None:
                    auth.login(request,user)

                    return redirect('dashboard')
     
     context = {'loginform':form}

     return render(request,'login.html',context=context)

     

def dashboard(request):
     template = loader.get_template('dashboard.html')
     return HttpResponse(template.render())