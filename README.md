
# Nathas, your Slack DJ
[![Code Climate](https://codeclimate.com/github/TeamSven/nathas/badges/gpa.svg)](https://codeclimate.com/github/TeamSven/nathas). 

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
