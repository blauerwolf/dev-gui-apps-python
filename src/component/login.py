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

    sg.theme('SystemDefault')
    window = login.build()
    #window["-TABLA_EXPEDIENTE-"].update(ingresar_expediente
