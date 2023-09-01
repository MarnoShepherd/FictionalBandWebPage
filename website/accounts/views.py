from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm

#views
def signup(request):
    """
    Handles user registration.

    If the HTTP request method is POST, it attempts to create a new user account
    using the provided form data. If the form data is valid, the user is registered,
    a success message is displayed, and the user is redirected to the login page.
    If the form data is invalid, an error message is displayed.

    If the request method is GET, it displays the registration form for users to fill out.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response, either displaying the registration form or
        redirecting the user to the login page.
    """
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
    """
    Handles user login.

    If the HTTP request method is POST, it attempts to authenticate the user using
    the provided username and password. If authentication is successful, the user
    is logged in, and they are redirected to the home page. If authentication fails,
    an error message is displayed.

    If the request method is GET, it displays the login form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response, either displaying the login form or
        redirecting the user to the home page.
    """
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
    """
    Handles user logout.

    Logs the user out of their account and displays a success message. After
    logging out, the user is redirected to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response, redirecting the user to the home page.
    """
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('home')

    

