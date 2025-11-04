from django.shortcuts import render, HttpResponse

# Create your views here.

def register_view(request):
    return HttpResponse("User Registration Page")

def login_view(request):
    return HttpResponse("User Login Page")

def logout_view(request):
    return HttpResponse("User Logout Page")

def profile_view(request):
    return HttpResponse("User Profile Page")