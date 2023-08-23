from django.shortcuts import render
from .models import Song

# Create your views here.
def songs(request):
    allSongs = Song.objects.all()
    return render(request, "songs.html", context={"allSongs" : allSongs})