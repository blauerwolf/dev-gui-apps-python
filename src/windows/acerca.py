import PySimpleGUI as sg
from os.path import join, dirname, abspath
from src.const.font import font_name, font_size

def build():
    sg.theme('LightBlue3')

    img_path = "src/static/g23112.png"
    boton_align_right = [ [sg.Button('Cerrar', key='close')] ]
    
    layout1 = [
        [ sg.Image(filename=img_path) ]
    ]
    
    layout2 = [
        [sg.Text('Ticket Killer', size=(100,1), justification='left', font=(font_name,16))],
        [sg.HorizontalSeparator()],
        [sg.Text('Ticket Killer es un sistema \nde registro de incidencias\nultraligero, portable\ny fácil de usar.', size=(100,15), justification='left')],
        [sg.Column(boton_align_right, vertical_alignment='right', justification='right')]
    ]
    
    layout = [
        [sg.Column(layout1, element_justification='c'), sg.Column(layout2, element_justification='c')],
        [sg.Sizegrip()]
    ]

    window = sg.Window('Aceca de Ticket Killer', layout, size=(450, 330))

    return window
