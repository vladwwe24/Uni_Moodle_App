from django.shortcuts import render

def index(request):
    return render(request, 'login_screen/start_screen.html')

def form(request):
    return render(request, 'login_screen/login_screen.html')
