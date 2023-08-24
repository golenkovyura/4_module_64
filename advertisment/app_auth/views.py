from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    pass


def profile_view(request):
    return render(request, 'app_auth/profile.html')


def logout_view(request):
    pass
