from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

engine = create_engine('sqlite:///myitems.db', echo=True)
Base = declarative_base()


class Item(Base):
    __tablename__="item"

    id = Column(Integer, primary_key=True)
    numb=Column(Integer)
    typename=Column(String)
    itemname=Column(String)
    size_i=Column(Integer)
    price=Column(Integer)

Base.metadata.create_all(engine)