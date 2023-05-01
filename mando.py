import socketio
import keyboard
import pyautogui

press = False
press1 = False
press2 = False
click1 = False
click2 = False

sio = socketio.Client()
sio.connect('https://apago-la-compu.onrender.com')
#sio.connect('http://localhost:5000')



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

@sio.event()
def compu_conexionsol():
    sio.emit("solicitoConexion")

@sio.on("conexionRecibida")
def conexion_recibida():
    print("computadora conectada")
    

def moverMouse():
    width, height = pyautogui.size()
    mouseX, mouseY = pyautogui.position()
    porcentajeX = mouseX / width
    porcentajeY = mouseY / height

    #print('Moviendo el mouse.')
    sio.emit('moverMouse', { "porcentajeX": porcentajeX, "porcentajeY": porcentajeY })
    
        

print('apretar la letra k para apagar compu')
print("apretar la letra c para cerrar sesion")
print("click derecho apretar l")
print("click izquierdo apretar j")
print("mantener ctrl para mover mouse")
count = 0
while True:
    count += 1
    

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
    
    if keyboard.is_pressed("ctrl") and count % 170 == 0:
        moverMouse()
    
    if press == False and keyboard.is_pressed('g'):
        press2 = True
        compu_conexionsol()
        
    if press == True and not keyboard.is_pressed('g'):
        press2 = False
    





