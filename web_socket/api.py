from web_socket import app , socketio
from flask_socketio import emit
import os
from flask import render_template

@app.route('/')
def index():
    return render_template('line_chart.html')

@socketio.on('page', namespace='/crawl')
def response(msg):
    print(msg)
    emit('response2',msg ,broadcast=True)

@socketio.on('my_event', namespace='/test')
def my_event(msg):
    os.system("python3 main.py")
    emit('message', {'data': "sussess"})


@socketio.on('total_page', namespace='/crawl')
def my_event(msg):
    emit('total_page', msg , broadcast=True)
