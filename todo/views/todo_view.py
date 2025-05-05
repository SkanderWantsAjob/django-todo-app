from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from ..models import TODOO

def todo_view_render(request):
    user = request.user

    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        TODOO.objects.create(title=title, user=user)
        return redirect('/todopage')

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

def change_status(request, srno):
    todo = get_object_or_404(TODOO, srno=srno)

    if todo.status == TODOO.Status.NOT_DONE:
        todo.status = TODOO.Status.PENDING
    elif todo.status == TODOO.Status.PENDING:
        todo.status = TODOO.Status.DONE
    else:
        todo.status = TODOO.Status.NOT_DONE

    todo.save()
    return redirect('/todopage')