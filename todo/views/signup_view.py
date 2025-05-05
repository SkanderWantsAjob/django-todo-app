from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup_view_render(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(fnm,email,pwd)
        my_user=User.objects.create_user(fnm,email,pwd)
        my_user.save()
        return redirect('/login')
    
    return render(request, 'signup.html')
