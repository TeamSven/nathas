import re
import youtube_search
import spotify_util

def get_artists(query):
    video_data = youtube_search.search({'q': query, 'max_results': 5})
    if video_data:
        tokens = []
        for datum in video_data:
            tokens.extend(re.split('[-|,]', datum[0]))
        tokens = set(tokens)

        artists = []
        for token in tokens:
            if is_artist(token.strip()):
                artists.append(token.strip().lower())

        return set(map(lambda x:x.title(), artists))

def is_artist(query):
    channel_data = youtube_search.search_list({'q': query, 'max_results': 1})
    if channel_data and len(channel_data) > 0:
        if re.search('topic', channel_data[0][0].lower()):
            return channel_data[0][1]
