import socketio
import keyboard

press = False


sio = socketio.Client('https://apago-la-compu.onrender.com')

@sio.event
def connect():
    print('Connected to server!')

@sio.event
def disconnect():
    print('Disconnected from server.')

@sio.event
def apagar_compu():
    print('Sending "apagar compu" event to server...')
    sio.emit('apagar compu')
sio.connect('http://localhost:5000')

print('Press the "K" key to turn off computer B.')
while True:
    if press == False and keyboard.is_pressed('k'):
        press = True
        apagar_compu()
        
    if press == True and not keyboard.is_pressed('k'):
        press = False