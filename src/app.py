from src.const.global_constants import *
from src.handlers.config import *
from src.handlers.models.usuario import *

def start():
    """
    Esta función es con la cual se comienza eligiendo cuál ser la primera ventana.
    """

    #print(postgresql)
    create()
    u = Usuario.find_user(username='pepito4')
    print(u.nombre)
    print(u.verify_password('1233'))
