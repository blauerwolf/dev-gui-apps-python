import PySimpleGUI as sg
from os.path import join, dirname, abspath

def build():
    sg.theme('LightBlue3')

    img_path = "src/static/g16989.png"
    imagen_centrada = [ sg.Image(filename=img_path, size=(128, 128)) ]
    botones_centrados = [ [sg.Button('Iniciar Sesion', key='login'), sg.Button('Cancelar', key='close')] ]
			
    layout = [
        [sg.Column([imagen_centrada], justification='center')],
        [sg.Text('Usuario:', size=(100, 1), justification='center')],
        [sg.InputText('', pad=((0,0), (0, 10)), key='user')],
        [sg.Text('Contraseña:', size=(100, 1), justification='center')],
        [sg.InputText('', password_char="*", key='password')],
        [sg.Column(botones_centrados, vertical_alignment='center', justification='center',  k='-C-')]
    ]	

    window = sg.Window('Login', layout, size=(250, 300))

    return window
