import re
import youtube_search
import spotify_util

def get_artists(query):
    video_data = youtube_search.search({'q': query, 'max_results': 5})
    print video_data
    if video_data:
        tokens = []
        for datum in video_data:
            tokens.extend(re.split('[-|,]', datum[0]))
        tokens = set(tokens)

        artists = []
        for token in tokens:
            if spotify_util.is_artist(token.strip()):
                artists.append(token.strip())

        return set(artists)
