from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.



def home(request):
	return render(request, "index.html")


def service(request):
    return render(request, "service.html")


def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact.objects.create(username=username, email=email, phone=phone, message=message)
        return redirect("/index/")

    return render(request, "contact.html")




def about(request):
    return render(request, "about.html")



def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('Login/')

        login(request, user)
        return redirect('home')

    return render(request, 'Login.html')



def user_logout(request):
    logout(request)
    return redirect('Login')



def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        organization_Name = request.POST.get('organization_Name')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            first_name = first_name,
            last_name = last_name,
            phone=phone,
            email=email,
            password=password,
            organization_Name = organization_Name
            # organname = organname
        )
        
        # Assuming 'phoneno' and 'orgname' are not fields in the default User model
        # If you want to store these fields, create a custom User model or a related model.

        messages.success(request, 'Account created successfully')
        return redirect('Login')

    return render(request, 'register.html')