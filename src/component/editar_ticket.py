import PySimpleGUI as sg
from src.windows import ingresar_ticket
from src.windows import editar_ticket
from src.handlers.models import ticket


def start(ticket_id):
    """
    Lanza la ejecución de la ventana
    """
    window = loop(ticket_id)
    window.close()


def loop(ticket_id):
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    
    window = editar_ticket.build(ticket_id)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-GUARDAR-':
            if (values['-DESCRIPCION-'] == "" or values['-CONTACTO-'] == "" or values['-USUARIO-'] == "" or values['-ESTADO-'] == ""):
                sg.popup_error("Teneś que completar todos los campos.", title="Error")
            else:
                ticket.actualizar_ticket(values)
                break

    return window

