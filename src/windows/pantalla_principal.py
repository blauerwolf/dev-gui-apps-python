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


    menu_def = [['&Archivo', ['!&Abrir', '&Guardar::guardarkey', '---', '&Propiedades', '&Salir']],
            ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Ventanas nuevas', ['Ventana &1', 'Ventana &2']],
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
                  #cols_justification=['c', 'l', 'c', 'c', 'c'],
                  headings=[" ID ", "     Descripcion     ", "   Contacto   ", " Usuario ", " Estado "],
                  row_height=20, num_rows=10, header_background_color="#FF8000", right_click_menu=[[],["Editar ticket", "Eliminar seleccion"]])],
        [sg.Text("""Seleccionar un elemento de la tabla y dar click derecho permite generar eventos especiales que permitiría
por ejemplo eliminar un expediente. VER EL MENSAJE DE LA CONSOLA PARA MAS INFORMACIÓN.""")]
    ]
    window = sg.Window('Sistema Integral v3.5', layout=layout, resizable=True, finalize=True)

    return window
