import PySimpleGUI as sg
from src.const.font import font_name, font_size


sg.theme('SystemDefault')

def build():

    categorias = [ "Creado", "En curso", "Cerrado", "Finalizado"]
    
    layout = [
        [sg.Text('Cargar incidente',font=(font_name,16))],
        [sg.HorizontalSeparator()],
        [sg.Text('id', size=(15,1)), sg.Spin(list(range(99999)), size=(10, 1), key="-ID-")],
        [sg.Text('Descripción', size=(15,1)), sg.Input(size=(30,1),key='-DESCRIPCION-')],
        [sg.Text('Contacto', size=(15,1)), sg.Input(size=(30,1),key='-CONTACTO-')],
        [sg.Text('Usuario', size=(15,1)), sg.Input(size=(30,1),key='-USUARIO-')],
        [sg.Text('Estado', size=(15,1)), sg.Combo(categorias,default_value=categorias[0],size=(24,1),key="-ESTADO-",readonly=True)],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    window = sg.Window('Cargar incidente', layout, font=(font_name,font_size), modal=True)
    return window