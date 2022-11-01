import PySimpleGUI as sg
from src.windows import pantalla_principal
from src.component import ingresar_ticket
from src.component import editar_ticket
from src.handlers.models import ticket


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
    window["-TABLA_TICKETS-"].update(ticket.leer_tickets())

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-INGRESAR_TICKET-':
            ingresar_ticket.start()
            window["-TABLA_TICKETS-"].update(ticket.leer_tickets())
  
        elif event == 'Eliminar seleccion' and window['-TABLA_TICKETS-'].get():
            if values["-TABLA_TICKETS-"]:

                ticket_seleccionado = window["-TABLA_TICKETS-"].get()[values["-TABLA_TICKETS-"][0]]
                msg = 'Estás seguro que querés eliminar el incidente # ' + str(ticket_seleccionado[0]) + '?'

                if sg.popup_ok_cancel(msg) == 'OK':
                    ticket.eliminar_ticket(ticket_seleccionado[0])
                    window["-TABLA_TICKETS-"].update(ticket.leer_tickets())
                
        elif event == 'Editar ticket' and window['-TABLA_TICKETS-'].get():
            if values["-TABLA_TICKETS-"]:
                ticket_seleccionado = window["-TABLA_TICKETS-"].get()[values["-TABLA_TICKETS-"][0]]
                editar_ticket.start(ticket_seleccionado[0])
                window["-TABLA_TICKETS-"].update(ticket.leer_tickets())

    return window

