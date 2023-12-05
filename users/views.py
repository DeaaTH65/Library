from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



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