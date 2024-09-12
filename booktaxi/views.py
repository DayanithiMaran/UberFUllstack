from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .  forms  import CreateUserForm,LoginForm


def IndexPage(request):

     return render(request,'booktaxi/index.html')


def register(request):
     
     form = CreateUserForm()
     if request.method == "POST":       
          form = CreateUserForm(request.POST)
          if form.is_valid():              
               form.save()
               return redirect("my-login")
               
     context={'registerform':form}           
     return render(request,'booktaxi/register.html',context=context)

    

def my_login(request):

     form = LoginForm()
     if request.method == 'POST':
          form = LoginForm(request, data=request.POST)
          if form.is_valid():
               username = request.POST.get('username')
               password = request.POST.get('password')

               user = authenticate(request, username=username,password=password)
               if user is not None:
                    auth.login(request,user)
                    return redirect("")
     context = {'loginform':form}
     return render(request,'booktaxi/my_login.html',context=context)

    
def User_Logout(request):
     auth.logout(request)
     return redirect("")
     

@login_required(login_url="my-login")
def HomePage(request):

     return render(request,'booktaxi/Home.html')

def profile(request):
  
     return render(request, 'booktaxi/profile.html')
   
def Construct(request):
     return render(request, 'booktaxi/development.html')
