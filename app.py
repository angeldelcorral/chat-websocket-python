import pytz

from datetime import datetime, timezone
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send, emit
from flask_cors import cross_origin

from views import manage_user

app = Flask(__name__)
socketio = SocketIO(app)


LOCAL_TIMEZONE = pytz.timezone('America/Santiago')

@socketio.on('new_message')
def handle_new_message(data):
    message = data['message']
    user_id = data['user_id']
    user_name = data['user_name']
    now = datetime.utcnow().replace(tzinfo=timezone.utc)
    time = now.astimezone(LOCAL_TIMEZONE)
    
    response_dict = {
        'message': message,
        'user_id': user_id,
        'user_name': user_name,
        'time': time.strftime("%H:%M")
    }
    emit('receive_message', response_dict, broadcast=True)

@app.route('/get_user_id', methods=['GET'])
@cross_origin(cross_origin="*")
def get_uuid():
    return manage_user.get_user_id()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)
