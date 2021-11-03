from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print('User created')
        return redirect("/")
    else:
        return render(request, 'register.html')
