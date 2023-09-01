from django.contrib import admin

from .models import Artist, Song, Album

# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """
    Admin class for managing Artist models.

    This admin class allows the management of Artist objects in the Django admin interface.
    It provides a customized display of Artist instances with specified fields.

    Attributes:
        list_display (tuple): A tuple specifying the fields to be displayed in the list view
            of Artist instances, including 'id', 'artistName', 'created', and 'last_updated'.
    """
    list_display = ("id", "artistName", "created", "last_updated")

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """
    Admin class for managing Song models.

    This admin class allows the management of Song objects in the Django admin interface.
    It provides a customized display of Song instances with specified fields.

    Attributes:
        list_display (tuple): A tuple specifying the fields to be displayed in the list view
            of Song instances, including 'id', 'album', 'song', 'songName', 'songThumbnail',
            'created', and 'last_updated'.
    """
    list_display = ("id", "album", "song", "songName", "songThumbnail", "created", "last_updated")

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """
    Admin class for managing Album models.

    This admin class allows the management of Album objects in the Django admin interface.
    It provides a customized display of Album instances with specified fields.

    Attributes:
        list_display (tuple): A tuple specifying the fields to be displayed in the list view
            of Album instances, including 'artist', 'albumName', 'created', and 'last_updated'.
    """
    list_display = ("artist", "albumName", "created", "last_updated")
