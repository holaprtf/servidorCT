import socketio
import keyboard
import pyautogui

press = False
press1 = False
mouseX, mouseY = pyautogui.position()

sio = socketio.Client()
sio.connect('https://apago-la-compu.onrender.com')

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

@sio.event()
def cerrar_sesion():
    print('cerrando sesion de computadora')
    sio.emit('cerrar sesion')

def moverMouse():
    newMouseX, newMouseY = pyautogui.position()
    diferenciaX = newMouseX - mouseX
    diferenciaY = newMouseY - mouseY
    mouseX = newMouseX
    mouseY = newMouseY

    if diferenciaX != 0 or diferenciaY != 0:
      sio.emit('moverMouse', { diferenciaX: diferenciaX, diferenciaY: diferenciaY })




    
        

print('Press the "K" key to turn off computer B.')
while True:
    
    

    if press == False and keyboard.is_pressed('k'):
        press = True
        apagar_compu()
        
    if press == True and not keyboard.is_pressed('k'):
        press = False


    if press1 == False and keyboard.is_pressed('c'):
        press1 == True
        cerrar_sesion()
    
    if press1 == True and not keyboard.is_pressed('c'):
        press1 = False

    moverMouse()
