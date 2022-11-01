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
    window["-TABLA_TICKETS-"].update(ticket.leer_tickets())

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-INGRESAR_TICKET-':
            ingresar_ticket.start()
            window["-TABLA_TICKETS-"].update(ticket.leer_tickets())

        elif event == '-EDITAR-TICKET-':
            print("editar ticket")
            #editar_ticket.start()
            
        elif event == 'Eliminar seleccion' and window['-TABLA_TICKETS-'].get():
            if values["-TABLA_TICKETS-"]:
                print(f'Fila selecciona de la tabla: {values["-TABLA_TICKETS-"][0]}')
                ticket_seleccionado = window["-TABLA_TICKETS-"].get()[values["-TABLA_TICKETS-"][0]]
                print(ticket_seleccionado)
                ticket.eliminar_ticket(ticket_seleccionado[0])
                window["-TABLA_TICKETS-"].update(ticket.leer_tickets())

    return window

