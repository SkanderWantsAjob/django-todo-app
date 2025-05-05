from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ..models import TODOO

def todo_view_render(request):
    user = request.user

    if request.method == 'POST':
        print("qqqqqqqqq")
        title = request.POST.get('title')
        print(title)
        TODOO.objects.create(title=title, user=user)

    res = TODOO.objects.filter(user=user).order_by('-date')
    return render(request, 'todo.html', {'res': res})

def delete_todo(request,srno):
    print(srno)
    obj=TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj =TODOO.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todopage')
    obj =TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})