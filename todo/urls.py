# todo/urls.py

from django.urls import path
from .views.signup_view import signup_view_render  # <-- This is the correct import
from .views.login_view import login_view_render
urlpatterns = [
    path('signup/', signup_view_render, name='signup'),
    path('login/', login_view_render, name='login')
]
