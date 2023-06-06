from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer,String,Numeric,create_engine
engine = create_engine('sqlite:///database.db')
factory = sessionmaker(bind=engine)
session = factory()
Base=declarative_base()
class Categories(Base):
     __tablename__="categories"
     code =Column(Integer,primary_key=True)
     description=Column(String(50))
class Book(Base):
    __tablename__="book"
    code=Column(Integer,autoincrement=True,primary_key=True)
    isbn =Column(Numeric(13))
    edition =Column(Integer)
    title =Column(String(300))
    authors =Column(String(300))
    category =Column(Integer,ForeignKey("categories.code"))
    price =Column(String(30))
    cover= Column(String(255), default='cover/'+edition+'.jpg')
if __name__=="__main__":                                                                         
    Base.metadata.create_all(engine)
    