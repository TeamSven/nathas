import os
import time
from slackclient import SlackClient
from pymongo import MongoClient

import commands

BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"

# BOT COMMANDS
HELLO_COMMAND = "hello"
HELP_COMMAND = "help"
LIST_COMMAND = "list"
RESUME_COMMAND = "resume"
PLAY_COMMAND = "play"
PAUSE_COMMAND = "pause"
NEXT_COMMAND = "next"
NEXT_COMMAND_1  = "play next"
CLEAR_COMMAND = "clear all"
VOLUME_UP_COMMAND = "volume up"
VOLUME_UP_COMMAND1 = "volumeup"
VOLUME_DOWN_COMMAND = "volume down"
VOLUME_DOWN_COMMAND1 = "volumedown"

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
mongo_client = MongoClient()
db = mongo_client['nathas']

def handle_command(command, user, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use `help` command"

    if command.startswith(HELLO_COMMAND):
        response = commands.hello()
    elif command.startswith(HELP_COMMAND):
        response = commands.help()
    elif command.startswith(LIST_COMMAND):
        response = commands.list()
    elif command.startswith(CLEAR_COMMAND):
        response = commands.clear_all()
    elif command.startswith(PAUSE_COMMAND):
        response = commands.pause()
    elif command.startswith(NEXT_COMMAND) or command.startswith(NEXT_COMMAND_1):
        response = commands.next()
    elif command.startswith(RESUME_COMMAND):
        response = commands.resume()
    elif command.startswith(PLAY_COMMAND):
        response = commands.play(slack_client, command, user, channel)
    elif command.startswith(VOLUME_UP_COMMAND) or command.startswith(VOLUME_UP_COMMAND1):
        response = commands.volume_up()
    elif command.startswith(VOLUME_DOWN_COMMAND) or command.startswith(VOLUME_DOWN_COMMAND1):
        response = commands.volume_down()

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            print output, "\n"
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['user'], \
                       output['channel']
    return None, None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("nathas connected and running!")
        while True:
            command, user, channel = parse_slack_output(slack_client.rtm_read())
            if command and user and channel:
                handle_command(command, user, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
