# todo/urls.py

from django.urls import path
from .views.signup_view import signup_view_render  # <-- This is the correct import
from .views.login_view import login_view_render
from .views.todo_view import todo_view_render, delete_todo, edit_todo
urlpatterns = [
    path('signup/', signup_view_render, name='signup'),
    path('login/', login_view_render, name='login'),
    path('todopage/', todo_view_render, name='todo'),
    path('delete_todo/<int:srno>',delete_todo, name="delete_todo"),
    path('edit_todo/<int:srno>', edit_todo, name='edit_todo')
]
