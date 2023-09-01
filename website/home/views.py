from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page.

    This view renders the 'home.html' template, which serves as the home page of
    the website.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response rendering the 'home.html' template.
    """
    return render(request, "home.html")

def about(request):
    """
    Render the about page.

    This view renders the 'about.html' template, which provides information about
    the website or organization.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response rendering the 'about.html' template.
    """
    return render(request, 'about.html')