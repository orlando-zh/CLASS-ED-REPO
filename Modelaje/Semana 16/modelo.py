from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Mascotas(Base):
    __tablename__= 'tbl_mascota'
    
    id = Column(Integer, primary_key=True)
    nombre= Column(String, nullable=False)
    raza=Column(String, nullable=False)
    
engine= create_engine('sqlite:///mascotadb', echo=True)

Base.metadata.create_all(engine)
