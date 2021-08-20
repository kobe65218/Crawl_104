from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, template_folder='./templates',static_folder='./static')
socketio = SocketIO(app)

from web_socket import api