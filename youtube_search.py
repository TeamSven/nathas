#!/usr/bin/python
import os

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = os.environ.get("YT_DEVELOPER_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def search_list(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=options['q'],
    part="id,snippet",
    type="channel",
    maxResults=options['max_results']
  ).execute()

  channels = get_list_from_search_response(search_responsem, "youtube#channel", "channelId")
  return channels


def search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=options['q'],
    part="id,snippet",
    maxResults=options['max_results']
  ).execute()

  videos = get_list_from_search_response(search_responsem, "youtube#video", "videoId")
  return videos


def get_list_from_search_response(response, kind, id):
  videos = []
  for search_result in response.get("items", []):
    if search_result["id"]["kind"] == kind:
      videos.append((search_result["snippet"]["title"], search_result["id"][id]))
  return videos

def get_top_tracks_for_channel(channel_id):
  playlist_id = get_channel_top_playlist(channel_id)

  if playlist_id is None:
      return

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  max_range = 10

  search_response = youtube.playlistItems().list(
    playlistId=playlist_id,
    part="contentDetails, snippet",
    maxResults=max_range
  ).execute()

  return [search_response['items'][i]['snippet']['title'] for i in xrange(max_range)]


def get_channel_top_playlist(channel_id):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.playlists().list(
    channelId=channel_id,
    part="contentDetails",
    maxResults=1
  ).execute()

  if len(search_response) > 0:
      return search_response['items'][0]['id']


if __name__ == "__main__":
  try:
    get_top_tracks_for_channel('UCfCNL5oajlQBAlyjWv1ChVw')
  except HttpError:
    print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
