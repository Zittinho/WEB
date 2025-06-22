from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.html import escape

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return HttpResponse('Invalid credentials')
    return render(request, 'users/login.html')

@login_required
def profile_view(request):
    
    request.session['last_seen'] = 'profile page'
    
    last = request.session.get('last_seen', 'nothing')
    return HttpResponse(f'Hello, {request.user.username}! Last: {last}')

def logout_view(request):
    logout(request)
    return redirect('login')

def safe_input_view(request):
    if request.method == 'POST':
        raw_input = request.POST['data']
        clean_input = escape(raw_input)  # Защита от XSS
        return HttpResponse(f'Clean: {clean_input}')
    return HttpResponse('Send POST data')

def upload_file_view(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        # Сохрани или обработай файл
        with open(f'temp/{uploaded_file.name}', 'wb+') as dest:
            for chunk in uploaded_file.chunks():
                dest.write(chunk)
        return HttpResponse('File uploaded')
    return HttpResponse('Upload a file')


