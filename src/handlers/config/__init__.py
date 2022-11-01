from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from src.const.global_constants import postgresql as settings

import logging

log = logging.getLogger(__name__)


def get_engine(user, passwd, host, port, db):
    """
    Obtiene el engine de SQLAlchemy usando las credenciales
    Input:
        user: Nombre de usuario de PostgreSQL
        passwd: Contraseña del usuario de PostgreSQL
        host: Nombre de host o IP donde corre PostgreSQL
        port: Puerto de PostgreSQL
        db: nombre de la base de datos
    Retorna:
        engine
    """
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)

    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_engine_from_settings():
    """
    Conecta la base de datos con los parámetros de global_constants.
    Input:
        Diccionario conteniendo pghost, pguser, pgpasswd, pgport y pgdb
    Retorna:
        engine
    """
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')

    return get_engine(settings['pguser'],
                    settings['pgpasswd'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])


def get_session():
    """
    Retorna una sesion de SQLAlchemy
    Input:
        engine: engine de SQLAlchemy
    """
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session 


def get_database():
    """
    Conecta a la base de datos.
    Devuelve:
        engine
    """
    try:
        engine = get_engine_from_settings()
        log.info("Connectado a PostgreSQL!")

    except IOError:
        log.exception("Falló la conexión a la DB.")
        return None, 'fail'

    return engine


db = get_database()
session = get_session()
Base = declarative_base()
