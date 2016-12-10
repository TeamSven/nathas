import os, re, time
import urllib2
from pymongo import MongoClient
import youtube_util

NATHAS_UI_ENDPOINT = os.environ.get("NATHAS_UI_ENDPOINT")
mongo_client = MongoClient()
db = mongo_client['nathas']

def hello():
    return "You say hello, I say world!"

def help():
    return "Type @nathas command [options] \n" + \
        "play [song name] \t \t to add a song to queue \n" + \
        "clear all \t \t to clear the queue"

def clear_all():
    db['playlist'].delete_many({})
    return "Sure, I have cleared the queue"

def play(command, user, channel):
    play_list_coll = db['playlist']
    request_record = {
        "requested_by": user,
        "requested_at": long(time.time())
    }

    request = ' '.join(command.split(' ')[1:])
    artist = ''
    try:
        request = re.search("(?P<url>https?://[^\s]+)", request).group("url")
        request_record["request_url"] = request
    except AttributeError:
        request_record["request_string"] = request
        artists = youtube_util.get_artists(request)

    play_list_coll.insert_one(request_record)

    prev_queue_size = play_list_coll.count() - 1

    if prev_queue_size == 0:
        response = 'Sure... \'' +  request + '\' will be played next'
    elif prev_queue_size == 1:
        response = 'Sure... \'' +  request + '\' will be played after 1 song'
    else:
        response = 'Sure... \'' +  request + '\' will be played after ' + str(prev_queue_size) + ' songs'

    print artists
    if len(artists) > 0:
        response += "\n The song was by `" + '`,`'.join(artists) + "`"

    return response

def pause():
    return "Not Yet Implemented"

def next():
    urllib2.urlopen(NATHAS_UI_ENDPOINT + "/next").read()
    return "Consider it done"
