from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import CustomUser
from django.contrib import messages
from .decorators import user_not_authenticated

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Hello <b>{user.first_name} {user.last_name}</b>! You have been logged in")
            return redirect('home') 
        
        else:
            return redirect('login.html')
        
    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
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
                messages.success(request, f"Hello <b>{user.email}</b>! Your account has been created and You have been logged in.")
                return redirect('home')
            else:
                # Email is already registered
                pass
        else:
            # Passwords do not match
            pass
    
    return render(request, 'users/register.html')



def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must type legit email to subscribe to a Newsletter")
            return redirect("/")
        
        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "/"))
        
        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))
        
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")
        
        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))