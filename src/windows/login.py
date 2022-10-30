import PySimpleGUI as sg

sg.theme('LightBlue3')

def iniciar_sesion(usuario, password):
    if(usuario == "" or password == ""):
        sg.popup_error("Debes completar los campos")
    else:
        if (usuario == "usuario1" and password == "1234"):
            sg.popup_ok("Usuario y contraseña correctos")
        else:
            sg.popup_error("Usuario o contraseña incorrectos")

imagen_centrada = [ sg.Image(filename='../static/g16989.png', size=(128, 128)) ]
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

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'close':
        break
    elif (event=='login'):
        iniciar_sesion(values['user'], values['password'])
