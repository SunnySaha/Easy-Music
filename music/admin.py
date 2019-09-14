from django.contrib import admin
from .models import Album, Song


class showInformatin(admin.ModelAdmin):
    list_display = ('user', 'artist', 'album_title', 'genre', 'is_favorite')


class showSongs(admin.ModelAdmin):
    list_display = ('album', 'song_title', 'audio_file', 'is_favorite')


admin.site.register(Album, showInformatin)
admin.site.register(Song, showSongs)
