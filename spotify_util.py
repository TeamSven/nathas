import spotipy
import sys

spotify = spotipy.Spotify()

def is_artist(token):
    results = spotify.search(q='artist:' + token, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        return True
    else:
        return False

def get_related_artists(token):
    results = spotify.search(q='artist:' + token, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        artist = items[0]
        related_artists = spotify.artist_related_artists(artist['uri'])
        if related_artists and related_artists['artists']:
            result = []
            for ra in related_artists['artists']:
                result.append(ra['name'])
            return result
