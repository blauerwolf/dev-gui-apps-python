from src.const.global_constants import *
from src.component import login
from src.handlers.config import *
from src.handlers.models.usuario import *


def start():
    """
    Esta función es con la cual se comienza eligiendo cuál ser la primera ventana.
    """
    login.start()
    
    

def initialize_db():
    create()
    u = Usuario.find_user(username='pepito4')
    print(u.nombre)
    print("Activo: %s", str(u.activo))
    print(u.verify_password('1233'))
    #u.disable_user()
    u.enable_user()
