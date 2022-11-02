import PySimpleGUI as sg
from src.const.font import font_name, font_size
from src.handlers.models import ticket
from src.handlers.models import usuario


sg.theme('LightBlue3')

def build(ticket_id):


    categorias = [ "Creado", "En curso", "Cerrado", "Finalizado"]
    categorias_keys = {}
    categorias_keys["Creado"] = 0
    categorias_keys["En curso"] = 1
    categorias_keys["Cerrado"] = 2
    categorias_keys["Finalizado"] = 3
    
    usuarios = []
    
    # Busco los usuarios para llenar el Combo
    u = usuario.leer_usuarios()
    for users in u:
        usuarios.append(users.nombre)
           
    
    # Busco el ticket en cuestión para rellenar el formulario
    t = ticket.buscar(ticket_id)
    cate = categorias_keys[t.estado]
    
    
    layout = [
        [sg.Text('Editar incidente',font=(font_name,16))],
        [sg.HorizontalSeparator()],
        [sg.Text('id', size=(15,1)), sg.Input(size=(30,1), key='-ID-', default_text=t.id, disabled=True)],
        [sg.Text('Descripción', size=(15,1)), sg.Input(size=(30,1),key='-DESCRIPCION-', default_text=t.descripcion)],
        [sg.Text('Contacto', size=(15,1)), sg.Input(size=(30,1),key='-CONTACTO-', default_text=t.contacto)],
        [sg.Text('Usuario', size=(15,1)), sg.Combo(usuarios, default_value=usuarios[t.usuario_id - 1], size=(24,1), key="-USUARIO-", readonly=True)],
        [sg.Text('Estado', size=(15,1)), sg.Combo(categorias,default_value=categorias[cate],size=(24,1),key="-ESTADO-",readonly=True)],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    window = sg.Window('Editar incidente', layout, font=(font_name,font_size), modal=True)
    return window