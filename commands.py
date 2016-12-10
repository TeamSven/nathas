import os, re, time
from pymongo import MongoClient

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
    try:
        request = re.search("(?P<url>https?://[^\s]+)", request).group("url")
        request_record["request_url"] = request
    except AttributeError:
        request_record["request_string"] = request

    play_list_coll.insert_one(request_record)

    prev_queue_size = play_list_coll.count() - 1
    if prev_queue_size == 0:
        return 'Sure... \'' +  request + '\' will be played next'
    elif prev_queue_size == 1:
        return 'Sure... \'' +  request + '\' will be played after 1 song'
    else:
        return 'Sure... \'' +  request + '\' will be played after ' + str(prev_queue_size) + ' songs'

def pause():
    return "Not Yet Implemented"

def next():
    return "Not Yet Implemented"
