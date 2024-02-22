from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'authentication/registration_error.html', {'error_message': 'Username is already taken'})

        # Create a new user (the password will be hashed automatically)
        user = User.objects.create_user(username=username, password=password, first_name=first_name)

        # Log in the user
        login(request, user)

        # Redirect to a success page (you can customize this)
        return HttpResponseRedirect(reverse('user_auth:show_user'))

    # If the request method is not POST, redirect to the login page
    return render(request, 'authentication/registration.html')

