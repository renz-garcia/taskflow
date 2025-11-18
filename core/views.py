from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def splash(request: HttpRequest) -> HttpResponse:
    return render(request, "core/splash.html")