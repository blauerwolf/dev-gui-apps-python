from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, \
    Enum, Float, ForeignKey, Integer, String, Text, TIMESTAMP, \
        UniqueConstraint, and_, func
from sqlalchemy.orm import relationship
from src.handlers.config import Base, db, session 

class Ticket(Base):
    __tablename__ = 'ticket'   
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(Text, nullable=False)
    contacto = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    created = Column(DateTime, nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP, onupdate=func.now(), default=None)
    deleted = Column(DateTime, nullable=True, default=None)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    parent = relationship("Usuario", back_populates="children")

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()
        return obj

    def actualizar_estado(self, estado):
        self.estado = estado
        session.commit()

    def actualizar_ticket(self, descripcion, contacto, estado, usuario_id):
        self.descripcion = descripcion 
        self.contacto = contacto 
        self.estado = estado 
        self.usuario_id = usuario_id
        session.commit()
        
    def borrar_ticket(self):
        self.deleted = func.now()
        session.commit()
        
    @classmethod
    def buscar_todos(cls):
        return session.query(cls).filter_by(deleted=None).all()
        

def create():
    Base.metadata.create_all(db)


def leer_tickets():
    tks = []
    
    t = Ticket.buscar_todos()

    for row in t:
        tks.append([row.id, row.descripcion, row.contacto, row.parent.nombre, row.estado])
    return tks
    
def buscar(ticket_id):
    return session.query(Ticket).filter_by(id=ticket_id).first()
    

def crear_ticket(ticket):

    tk = Ticket.create(descripcion=ticket['-DESCRIPCION-'],
                        contacto=ticket['-CONTACTO-'],
                        estado=ticket['-ESTADO-'],
                        usuario_id=ticket['-USUARIO-'])
    return tk.id

    
def eliminar_ticket(id):
    t = session.query(Ticket).filter_by(id=id).first()
    t.borrar_ticket()


def actualizar_estado(id, estado):
    t = session.query(Ticket).filter_by(id=id).first()
    t.actualizar_estado(estado)


def actualizar_ticket(ticket):
    t = session.query(Ticket).filter_by(id=ticket['-ID-']).first()
    t.actualizar_ticket(descripcion=ticket['-DESCRIPCION-'],
                        contacto=ticket['-CONTACTO-'],
                        estado=ticket['-ESTADO-'],
                        usuario_id=ticket['-USUARIO-'])


create()
