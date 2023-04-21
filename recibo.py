import socketio
import os
from ctypes import windll

EWX_LOGOFF = 0

sio = socketio.Client()
sio.connect('https://apago-la-compu.onrender.com')

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

@sio.on('cerrar secion')
def cerrar_secion():
    print('cerrando secion')
    windll.user32.ExitWindowsEx(EWX_LOGOFF, 0)

while True:
    pass