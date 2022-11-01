from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, \
    Enum, Float, ForeignKey, Integer, String, Text, TIMESTAMP, \
        UniqueConstraint, and_, func
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from src.handlers.config import Base, db, session 

class Ticket(Base):
    __tablename__ = 'ticket'   
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(Text, nullable=False, unique=True)
    contacto = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    created = Column(DateTime, nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP, onupdate=func.now())
    deleted = Column(DateTime, nullable=True)

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()

def create():
    Base.metadata.create_all(db)

create()