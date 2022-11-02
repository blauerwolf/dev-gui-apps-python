import PySimpleGUI as sg
from src.windows import acerca

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
    window = acerca.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break
        elif event == sg.WIN_CLOSED or event == 'close':
            break
        
    return window

                
