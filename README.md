
# Nathas, your Slack DJ
[![Code Climate](https://codeclimate.com/github/TeamSven/nathas/badges/gpa.svg)](https://codeclimate.com/github/TeamSven/nathas)  ![MIT](https://img.shields.io/dub/l/vibe-d.svg)

![Nathas](nathas.png)

## What does it do?

* Nathas provides a Slack bot to sit on your slack channel and listen to your teams music request. Nathas queue up your requests and stream them for your team all day long.
* [Nathas Frontend](https://github.com/TeamSven/nathas-frontend) provide a web application for your to enjoy the music chosen by your team. 
* When you run out of songs, Nathas will come to resue with music suggestion based on your team's music taste.

## Usage

### 1. Creating 3rd party accounts

- Create a Slack Bot for your team.
- Create a project on Google Developer console to access YouTube.

### 2. Download the code
Clone or fork this repo to your machine and install the dependencies.
```
pip install -r requirements.txt
```

### 3. Environmental Variables

* `SLACK_BOT_TOKEN`: This is the HTTP API Token you obtained when creating the bot.  
* `BOT_ID`: Once you have created a Slack Bot, *run get_bot_id.py*.  
* `YT_DEVELOPER_KEY`: Youtube developer key to access Data API.  
* `NATHAS_UI_ENDPOINT`: IP address and port number of the UI application.  

### 4. Commands available
```
$ @nathas command [options] 

list          list the songs in the queue
play _[song]_ to add a song to queue
clear all     to clear the queue
next          to play the next song
pause         to pause the current song
resume        to resume the paused song
suggest       to get song suggestion
shuffle       to shuffle your song queue
volumeup      to increase the volume of the player
volumedown    to decrease the volume of the player
```

## Views

### Get help
<div>
  <img src="screenshots/help.png" height="60%" width="60%">
</div>

### List queue
<div>
  <img src="screenshots/list.png" height="90%" width="90%">
</div>

### Play next 
<div>
  <img src="screenshots/next.png" height="40%" width="40%">
</div>

### Play an artist
<div>
  <img src="screenshots/artist.png" height="90%" width="90%">
</div>

### Play all
<div>
  <img src="screenshots/playall.png" height="30%" width="30%">
</div>

### Play a song
<div>
  <img src="screenshots/play.png" height="40%" width="40%">
</div>

### Resume song
<div>
  <img src="screenshots/resume.png" height="60%" width="60%">
</div>

### Shuffle the queue
<div>
  <img src="screenshots/shuflle.png" height="30%" width="30%">
</div>

### Get suggestion
<div>
  <img src="screenshots/suggest.png" height="90%" width="90%">
</div>

### Control volume
<div>
  <img src="screenshots/volumeup.png" height="30%" width="30%">
</div>
