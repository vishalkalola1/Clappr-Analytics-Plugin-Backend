from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_handlers=True)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on("message")
def handleMessage(data):
    emit("new_message",data,broadcast=True)


@socketio.on("offlineevents")
def handle_offlinedata(messages):
    return messages


@socketio.on("events")
def handle_Channel1(message):
    return message


@socketio.on("connect")
def test_connect():
    print("User Connected")


@socketio.on("disconnect")
def test_disconnect():
    print('user Disconnected')

    
if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
