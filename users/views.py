from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .decorators import user_not_authenticated



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return redirect('login.html')
        
    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


@user_not_authenticated
def user_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if not CustomUser.objects.filter(email=email).exists():
                # Create a new user
                user = CustomUser.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password1
                )
                # Authenticate and log in the user
                authenticate_user = authenticate(request, username=email, password=password1)
                login(request, authenticate_user)
                return redirect('home')
            else:
                # Email is already registered
                pass
        else:
            # Passwords do not match
            pass
    
    return render(request, 'users/register.html')
