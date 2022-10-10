from flask import Flask, request
from flask_socketio import SocketIO, send, disconnect
from difflib import get_close_matches
import pandas as pd
import sqlite3
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xe7\xab\x01\xf9\x18\xbb'
socketio = SocketIO(app, cors_allowed_origins = '*')

con = sqlite3.connect("qa.sqlite3")

dataframe = pd.read_sql_query("SELECT question, answer FROM qa_pair", con)

last_msg = {}
waiting_time = 10

@socketio.on('connect')
def welcomeMessage(auth):
    if auth['token'] == 'password123':
        send("hello there", broadcast = False)
    else:
        send("wrong password", broadcast = False)
        disconnect()

@socketio.on('message')
def handleMessage(msg):

    q = get_close_matches(msg, dataframe['question'])

    if q:
        ans = dataframe.loc[dataframe['question'] == q[0], 'answer'].iloc[0]
        send(ans, broadcast=False)
    else:
        send("sorry, I don't understand what you're saying", broadcast = False)

    print(request)
    last_msg[request.sid] = time.time()

def idle_check_thread():
    while True:
        current_time = time.time()
        try:
            for e in last_msg:
                if (last_msg[e] + waiting_time) < current_time:
                    socketio.send("are you there?", to = e)
                    last_msg.pop(e)
        except:
            pass

x = threading.Thread(target=idle_check_thread)
x.start()

if __name__ == '__main__':
    socketio.run(app)