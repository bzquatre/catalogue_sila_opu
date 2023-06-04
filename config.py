from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer,String,Numeric,create_engine
engine = create_engine('sqlite:///database.db')
factory = sessionmaker(bind=engine)
session = factory()
Base=declarative_base()
class Disciplins(Base):
     __tablename__="disciplins"
     code_disciplin =Column(Integer,primary_key=True)
     desgination_disciplin=Column(String(50))
class Livre(Base):
    __tablename__="livre"
    code_livre=Column(Integer,autoincrement=True,primary_key=True)
    isbn_article =Column(Numeric(13))
    edition_article =Column(Integer)
    titre_article =Column(String(300))
    auteur_article =Column(String(300))
    disciplin =Column(Integer,ForeignKey("disciplins.code_disciplin"))
    prix_ttc =Column(String(30))
if __name__=="__main__":                                                                         
    Base.metadata.create_all(engine)
    