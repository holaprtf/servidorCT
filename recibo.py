import socketio
import os
from ctypes import windll
import pyautogui

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

@sio.on('cerrar sesion')
def cerrar_sesion():
    print('cerrando sesion')
    windll.user32.ExitWindowsEx(EWX_LOGOFF, 0)

@sio.on('click izquierdo')
def click_izquierdo():
    pyautogui.click(button='left')

@sio.on('click derecho')
def click_derecho():
    pyautogui.click(button='right')



while True:
    pass