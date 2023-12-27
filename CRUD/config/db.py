from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import MetaData

meta = MetaData()


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Himanshu!pal2002@localhost:3306/employee"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# engine = create_engine('mysql+mysqlconnector://root:Him20@12@localhost/test')
