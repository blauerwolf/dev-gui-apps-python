from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, \
    Enum, Float, ForeignKey, Integer, String, UniqueConstraint, and_, func
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from src.handlers.config import Base, db, session 

class Usuario(Base):
    __tablename__ = 'usuario'   
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)

    # Constructor
    def __init__(self, nombre, password, activo):
        self.nombre = nombre
        self.password = generate_password_hash(password, method='sha256')
        self.activo = activo

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()

    def find_user(username):
        return session.query(Usuario).filter_by(nombre=username).first()

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def disable_user(self):
        self.activo = False
        #session.query(self).update({ self.activo: False})
        #session.query(Usuario).filter_by(username=username).first().update({ activo: False})
        session.commit()

    def enable_user(self):
        self.activo = True
        session.commit()


def create():
    Base.metadata.create_all(db)

create()