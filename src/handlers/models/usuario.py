from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, \
    Enum, Float, ForeignKey, Integer, String, UniqueConstraint, and_, func
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from src.handlers.config import Base, db, session 

class Usuario(Base):
    __tablename__ = 'usuario'
    
    #_password = Column("password", String(256), nullable=False)

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    activo = Column(Boolean, nullable=False)

    # Constructor
    def __init__(self, nombre, password, activo):
        self.nombre = nombre
        self.password = generate_password_hash(password, method='sha256')
        self.activo = activo

    #@property
    #def password(self):
    #    raise AttributeError('Password is not a readable attribute')

    #@password.setter
    #def password(self, password):
    #    self._password = generate_password_hash(password, method='sha256')

    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()

    
    def find_user(username):
        return session.query(Usuario).filter_by(nombre=username).first()

    #def login(username, password):
    #    u = session.query(Usuario).filter_by(nombre=username).first()


    def verify_password(self, password):
        return check_password_hash(self.password, password)

    #def get_nombre(self):
    #    return self.nombre

    @classmethod
    def login(cls, user, password):
        user = session.query(Usuario).filter_by(nombre=user).first()

        if cls.verify_password(cls, password=password):

        #if check_password_hash(user.password, password):
            print('coincide')
        else:
            print('No coincide')

        print(user.password)


def create():
    Base.metadata.create_all(db)

create()