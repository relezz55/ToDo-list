from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///task.db"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class Task(Base):
    __tablename__ = "задача"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    user_id = Column(Integer)
    task_id = Column(Integer)

class User(Base):
    __tablename__ = "пользователи"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)

# Task.__table__.drop(engine)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

