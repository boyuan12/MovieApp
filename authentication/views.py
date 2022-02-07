from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":

        user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])

        login(request, user)

        return HttpResponse("success")

    else:
        return render(request, "authentication/register.html")

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(usename=username, password=password)

        if user is not None:
            login(request, user)
        else:
            return HttpResponse("wrong username or password")

        return HttpResponse("success")

    else:
        return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    return HttpResponse("logged out successfully")