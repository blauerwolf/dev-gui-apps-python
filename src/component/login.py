import PySimpleGUI as sg
from src.handlers.models.usuario import *
from src.windows import login

def start():
    """
    Lanza la ejecución de la ventana
    """
    window = loop()
    window.close()

    
def loop():
    """
    Loop de la ventana
    """

    sg.theme('LightBlue3')
    window = login.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break
        elif event == sg.WIN_CLOSED or event == 'close':
            print("cierra")
            break
        elif event == '-PANTALLA_PRINCIPAL-':
            print("hola")
            break
        elif event=='login':
            iniciar_sesion(values['user'], values['password'])

    return window
    #window["-TABLA_EXPEDIENTE-"].update(ingresar_expediente


def iniciar_sesion(usuario, password):
    if(usuario == "" or password == ""):
        sg.popup_error("Debes completar los campos")
    else:
        u = Usuario.find_user(username=usuario)
        if not u:
            sg.popup_error("Usuario o contraseña incorrectos")
        else:
            if not u.verify_password(password):
                sg.popup_error("Usuario o contraseña incorrectos")
            else:
                sg.popup_ok("Usuario y contraseña correctos")
                