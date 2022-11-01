from src.const.global_constants import *
from src.component import login
from src.component import pantalla_principal
from src.handlers.config import *
from src.handlers.models.usuario import *


def start():
    """
    Esta función es con la cual se comienza eligiendo cuál ser la primera ventana.
    """
    login.start()
    pantalla_principal.start()
    
    

def initialize_db():
    create()


def seed_db():
    """
    Creo unos usuarios de prueba.
    Default password: password
    """
    u = Usuario.find_user(username='admin')
    if not u:
        Usuario.create(nombre='admin', password='password', activo=True)

    u = Usuario.find_user(username='operador')
    if not u:
        Usuario.create(nombre='operador', password='password', activo=True)
        
    u = Usuario.find_user(username='consulta')
    if not u:
        Usuario.create(nombre='consulta', password='password', activo=True)
