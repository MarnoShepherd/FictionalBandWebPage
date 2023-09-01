from django.shortcuts import render
from .models import Song

# Create your views here.
def songs(request):
    """
    Render a list of songs.

    This view retrieves all the Song objects from the database using the Song model's
    manager (all() method) and renders them in a template named 'songs.html'. The
    retrieved songs are passed to the template as a context variable named 'allSongs'.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response rendering the 'songs.html' template with a context
        containing all the songs retrieved from the database.
    """
    allSongs = Song.objects.all()
    return render(request, "songs.html", context={"allSongs" : allSongs})