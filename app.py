from flask import Flask, render_template, request
from flask_socketio import SocketIO
#from camera import Camera

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sennagang_pkpap'
socketio = SocketIO(app)

# intialising client ip
CLIENT_IP = "0.0.0.0"

# list of valid user commands
VALID_USER_COMMANDS = ['left', 'right', 'up', 'down']


def handle_user_command(cmd):
    ''' Function to handle valid user chat commands
        TBD: Based on user commands, drive motor (i.e change Pi GPIO outputs)
    '''
    print "Command: {}".format(cmd)

@app.route('/')
def chat():
    ''' Function to render the initial screen of this app '''
    return render_template('chat.html')

@socketio.on('connect_event')
def handle_connect_event(json, methods=['GET', 'POST']):
    ''' Function to handle initial client connection '''
    global CLIENT_IP
    CLIENT_IP = request.remote_addr
    print('Client connected! : {}, First client msg: {}'.format(CLIENT_IP, json))

@socketio.on('chat_event')
def handle_chat_event(json, methods=['GET', 'POST']):
    ''' Function to handle chat events
        If valid commands are entered, the commands will be displayed on above the chat window
        Also calls the RPi motor functionality
    '''
    global CLIENT_IP
    print('Client : {}, Received data : {}'.format(CLIENT_IP, json))
    json.update({'client_ip' : CLIENT_IP})
    try:
	cmd = json['command']
    except KeyError as e:
        print("Error: {}".format(e))
        return

    if cmd.lower() not in VALID_USER_COMMANDS:
	print("Error: Invalid command : {}".format(cmd))
        return

    handle_user_command(cmd)

    socketio.emit('server_response_event', json, callback=None)


def gen(camera):
    ''' Video streaming generator function '''
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    ''' Video streaming route. '''
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80, debug=True)
