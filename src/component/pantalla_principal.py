import PySimpleGUI as sg
from src.windows import pantalla_principal
from src.component import ingresar_ticket
from src.handlers.models import ticket
#from src.component import ingresar_expediente
#from src.handlers import ingresar_expediente_handler


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
    sg.theme('SystemDefault')

    window = pantalla_principal.build()
    #window["-TABLA_TICKETS-"].update(ingresar_expediente_handler.leer_archivo())

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-INGRESAR_TICKET-':
            ingresar_ticket.start()
            #window["-TABLA_EXPEDIENTE-"].update(ingresar_expediente_handler.leer_archivo())

        elif event == '-EDITAR-TICKET-':
            print("editar ticket")
            #editar_ticket.start()

    return window
