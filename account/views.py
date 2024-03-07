from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, ('Tài khoản hoặc mật khẩu của bạn không chính xác!'))
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html',{})
    
@login_required(login_url='login_user')
def dashboard(request):
    context={}
    return render(request,'home/dashboard.html', context)
    
