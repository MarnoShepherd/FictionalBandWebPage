from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm

#views
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created succesfully")
            return redirect('login_user')
        else:
            messages.error(request, "There was an error registering, please try again or try logging in.")
    else:
        form = SignupForm()
    return render(request, "accounts/register.html", {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error loging in, please try again."))
            return redirect('login_user')

    else:
        return render(request, "accounts/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('home')

    

