from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request , "home/index.html")

def register_page(request):
   if request.method == "POST":
     uname=request.POST.get('username')
     email=request.POST.get('email')
     pass1=request.POST.get('password')
     my_user = User.objects.create_user(uname,email,pass1)
     my_user.save()
     
     return redirect('login_page')

       
   
   return render(request , "home/register.html")

def login_page(request):
   if request.method == "POST":
      username=request.POST.get('username')
      pass1=request.POST.get('password')
     
      user=authenticate(request,username=username,password=pass1)
      if user is not None:
        login(request,user)
        return redirect('dashboard_page')
      else:
         return HttpResponse("Username or Pass is incorrect")
         
      
     
   return render(request , "home/login.html")


def logout_page(request):
   logout(request)
   return redirect('login_page')