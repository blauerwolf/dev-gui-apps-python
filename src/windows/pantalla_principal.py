from datetime import date
import PySimpleGUI as sg
from src.const import font


def build():
    """
    Construye la ventana principal
    """
    # El theme siempre hay que ponerlo primero, sino no funciona
    sg.theme('LightBlue3')

    font16 = ("Calibri Italic", 16)


    menu_def = [['&Archivo', ['&Cargar Tk', '!&Guardar::guardarkey', '---', '&Salir']],
            ['!&Edición', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Ayuda', '&Acerca de...'], ]

    layout = [
        [sg.Menu(menu_def)],
        [sg.Text(f'Incidentes', font=(font.font_name, 16), size=(30, 1))],
        [sg.HorizontalSeparator()],
        [sg.Text("Elija alguna opción del menu superior.")],
        [sg.Button("Cargar ticket", key='-INGRESAR_TICKET-', tooltip='Permite cargar un nuevo ticket de un cliente',
                      font=(font.font_name, 11)),
        ],
        [sg.Table(values=[["-", "-", "-", "-", "-"]], key="-TABLA_TICKETS-",
                  justification="c",
                  headings=[" ID ", "     Descripcion     ", "   Contacto   ", " Usuario ", " Estado "],
                  row_height=20, num_rows=10, header_background_color="#FF8000", right_click_menu=[[],["Editar ticket", "Eliminar seleccion"]])],
        [sg.Text("""Seleccionar un elemento de la tabla y dar click con el botón secundario del mouse para editar o eliminar el incidente.""")]
    ]
    window = sg.Window('Ticket Killer v3.5', layout=layout, resizable=True, finalize=True)

    return window
