import socketio
import os

sio = socketio.Client()
sio.connect('http://localhost:5000')

@sio.on('connect')
def connect():
    print('conectado server')

@sio.on('disconnect')
def disconnect():
    print('server desconectado')

@sio.on('apagar compu')
def apagar_compu():
    print('apagando la compu')
    os.system('shutdown /s /t 1')

while True:
    pass