from flask import Flask, render_template, request
from flask_socketio import SocketIO
import time
from bot import Bot


# initialising client ip
CLIENT_IP = "0.0.0.0"

# list of valid user commands
VALID_USER_COMMANDS = ['left', 'right', 'up', 'down']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sennagang_pkpap'
socketio = SocketIO(app)


def handle_user_command(cmd):
    """ Function to handle valid user chat commands. Based on user commands, drive bot in that direction
        returns -1 for invalid command
                 0 for valid command
    """

    print "User command is : {}".format(cmd)
    cmd = str(cmd).lower()

    if cmd not in VALID_USER_COMMANDS:
        print "Invalid command : {}".format(cmd)
        return -1

    if cmd == "up":
        bot.move_forward()
    elif cmd == "down":
        bot.move_backward()
    elif cmd == "left":
        bot.turn_left()
    elif cmd == "right":
        bot.turn_right()
    else:
        print "Invalid command : {}".format(cmd)
        return -1

    print "Executed command!"
    return 0


@app.route('/')
def chat():
    """ Function to render the initial screen of this app. Screen consists a chat window and a video feed window """

    return render_template('chat.html')


@socketio.on('connect_event')
def handle_connect_event(json, methods=['GET', 'POST']):
    """ Function to handle initial client connection """

    global CLIENT_IP
    CLIENT_IP = request.remote_addr
    print "Client connected! : {}, First client msg: {}".format(CLIENT_IP, json)


@socketio.on('chat_event')
def handle_chat_event(json, methods=['GET', 'POST']):
    """ Function to handle chat events. If valid commands are entered, commands will be displayed in the chat window
        Also calls the function to move bot
    """
    global CLIENT_IP
    print "Client : {}, Received data : {}".format(CLIENT_IP, json)
    json.update({'client_ip': CLIENT_IP})
    try:
        cmd = json['command']
    except KeyError as e:
        print "Error: {}".format(e)
        return -1

    handle_user_command(cmd)

    socketio.emit('server_response_event', json, callback=None)


def bot_init():
    """
    Function to initialize Bot hardware
    1. init motors
    2. init Camera (TBD)
    """
    return Bot()


if __name__ == '__main__':
    """Initialize Bot"""
    print "Starting Bot..."
    bot = bot_init()
    time.sleep(1)

    socketio.run(app, host='0.0.0.0', port=80, debug=True)
