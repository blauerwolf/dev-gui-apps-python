import PySimpleGUI as sg
from src.windows import ingresar_ticket
from src.handlers.models import ticket
from src.handlers.models import usuario


def start():
    """
    Lanza la ejecución de la ventana
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    
    window = ingresar_ticket.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-GUARDAR-':
            
            if (values['-DESCRIPCION-'] == "" or values['-CONTACTO-'] == "" or values['-USUARIO-'] == "" or values['-ESTADO-'] == ""):
                sg.popup_error("Teneś que completar todos los campos.", title="Error")
            else:
                user_id = usuario.buscar_usuario(values['-USUARIO-']).id
                values["-USUARIO-"] = user_id
                tk_id = ticket.crear_ticket(values)
                break

    return window

