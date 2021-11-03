from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            print("success")
            messages.info(request, 'Successful login')
            return render(request, 'index.html', {'username':username})
        else:
            print('Invaid credential')
            messages.info(request, 'Unsuccessful login')
            return render(request, 'login.html')
    else:
        messages.info(request, 'Unsuccessful login')
        return render(request, 'login.html')
    