from django.db import models
from django.utils.translation import gettext_lazy as _

class Artist(models.Model):
    """
    Model representing an artist.

    Attributes:
        artistName (CharField): The name of the artist.
        created (DateTimeField): The date and time when the artist was created.
        last_updated (DateTimeField): The date and time when the artist information was last updated.

    Meta:
        verbose_name (str): A human-readable name for the model, set to "Artist".
        verbose_name_plural (str): A human-readable name for the model in plural form, set to "Artists".

    Methods:
        __str__(): Returns a string representation of the artist, which is the artist's name.
    """
    artistName = models.CharField(_("Artist Name"), max_length=50)
    created = models.DateTimeField(_("Artist created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Artist created date"), auto_now=True)

    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")

    def __str__(self):
        return self.artistName
    

class Album(models.Model):
    """
    Model representing an album.

    Attributes:
        artist (ForeignKey): A foreign key relationship to the Artist model, representing the album's artist.
        albumName (CharField): The name of the album.
        created (DateTimeField): The date and time when the album was created.
        last_updated (DateTimeField): The date and time when the album information was last updated.

    Meta:
        verbose_name (str): A human-readable name for the model, set to "Album".
        verbose_name_plural (str): A human-readable name for the model in plural form, set to "Albums".

    Methods:
        __str__(): Returns a string representation of the album, which is the album's name.
    """
    artist = models.ForeignKey("Artist", verbose_name = ("Artist Album"), on_delete=models.CASCADE)
    albumName = models.CharField(_("Album Name"), max_length=50)
    created = models.DateTimeField(_("Album created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest album update"), auto_now=True)

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")

    def __str__(self):
        return self.albumName
    

class Song(models.Model):
    """
    Model representing a song.

    Attributes:
        album (ForeignKey): A foreign key relationship to the Album model, representing the song's album.
        songThumbnail (ImageField): An image field for the song's thumbnail with upload path 'thumbnail/'.
        song (FileField): A file field for the song with upload path 'music/'.
        songName (CharField): The name of the song.
        created (DateTimeField): The date and time when the song was created.
        last_updated (DateTimeField): The date and time when the song information was last updated.

    Meta:
        verbose_name (str): A human-readable name for the model, set to "Song".
        verbose_name_plural (str): A human-readable name for the model in plural form, set to "Songs".

    Methods:
        __str__(): Returns a string representation of the song, which is the song's name.
    """
    album = models.ForeignKey("Album", verbose_name = ("Song Album"), on_delete=models.CASCADE)
    songThumbnail = models.ImageField(_("Song Thumbnail"), upload_to='thumbnail/', help_text=".jpg, .png, .jpeg, .gif, .svg supported")
    song = models.FileField(_("Song"), upload_to='music/', help_text=".wav supported only")
    songName = models.CharField(_("Song Name"), max_length=50)
    created = models.DateTimeField(_("Song created date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Latest song update"), auto_now=True)

    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

    def __str__(self):
        return self.songName