import PySimpleGUI as sg
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
            iniciar_sesion('usuario1','1234')

    return window
    #window["-TABLA_EXPEDIENTE-"].update(ingresar_expediente


def iniciar_sesion(usuario, password):
    if(usuario == "" or password == ""):
        sg.popup_error("Debes completar los campos")
    else:
        if (usuario == "usuario1" and password == "1234"):
            sg.popup_ok("Usuario y contraseña correctos")
        else:
            sg.popup_error("Usuario o contraseña incorrectos")