import socketio
import keyboard
import pyautogui

press = False
press1 = False
click1 = False
click2 = False
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


@sio.event()
def click_izquierdo():
    sio.emit('click izquierdo')


@sio.event()
def click_derecho():
    sio.emit('click derecho')



def moverMouse():
    newMouseX, newMouseY = pyautogui.position()
    diferenciaX = newMouseX - mouseX
    diferenciaY = newMouseY - mouseY
    mouseX = newMouseX
    mouseY = newMouseY

    if diferenciaX != 0 or diferenciaY != 0:
      sio.emit('moverMouse', { diferenciaX: diferenciaX, diferenciaY: diferenciaY })




    
        

print('apretar la letra k para apagar compu')
print("apretar la letra c para cerrar sesion")
print("apretar j para click izquierdo")
print('apretar l para click derecho')
while True:
    
    

    if press == False and keyboard.is_pressed('k'):
        press = True
        apagar_compu()
        
    if press == True and not keyboard.is_pressed('k'):
        press = False


    if press1 == False and keyboard.is_pressed('c'):
        press1 = True
        cerrar_sesion()
    
    if press1 == True and not keyboard.is_pressed('c'):
        press1 = False 
    
    if click1 == False and keyboard.is_pressed('j'):
        click1 = True
        click_izquierdo()
    
    if click1 == True and not keyboard.is_pressed('j'):
        click1 = False
    
    
    if click2 == False and keyboard.is_pressed('l'):
        click2 = True
        click_derecho()
    
    if click2 == True and not keyboard.is_pressed('l'):
        click2 = False





