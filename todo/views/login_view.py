from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view_render(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        user=authenticate(request,username=fnm,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('/todopage')
        else:
            return redirect('/login')
            
    return render(request, 'login.html')