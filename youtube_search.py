#!/usr/bin/python
import os

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = os.environ.get("YT_DEVELOPER_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def search_list(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options['q'],
    part="id,snippet",
    type="channel",
    maxResults=options['max_results']
  ).execute()

  channels = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#channel":
      channels.append((search_result["snippet"]["title"], search_result["id"]["channelId"]))

  return channels


def search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options['q'],
    part="id,snippet",
    maxResults=options['max_results']
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append((search_result["snippet"]["title"], search_result["id"]["videoId"]))

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
  except HttpError, e:
    print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
