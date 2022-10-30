from src.const.global_constants import *
from src.handlers.config import *

def start():
    """
    Esta función es con la cual se comienza eligiendo cuál ser la primera ventana.
    """

    print('hola')
    db = get_session()
    print(postgresql)