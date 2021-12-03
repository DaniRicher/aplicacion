from sqlalchemy import Column, Integer, String
from app.database.sessions import Base

class Place(Base):
    __tablename__= "places"
    id= Column(Integer, primary_key=True, index=True)
    name= Column(String, index=True)
    descripcion = Column(String)
    image = Column(String)