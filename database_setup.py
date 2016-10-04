from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HEREc

class Users(Base):
	__tablename__ = 'person'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	password = Column(String)
	birthday = Column(Date)
	score = Column(Integer)
	username = Column(String)
	slogan = Column(String)
	course_height = Column(Integer)  
	pic = Column(String)
	horse = Column(String)
	club = Column(String)
	history = Column(String)

class Admin(Base):
	__tablename__ = 'admin'
	id = Column(Integer,primary_key=True)
	username = Column(String)
	password = Column(String)


class Horses(Base):
	__tablename__ = 'horses'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	birthday = Column(Date)
	height = Column(Integer)
	max_jump = Column(Integer)
	course_height = Column(Integer)
	pic = Column(String)
	owner = Column(String)


class Data(Base):
	__tablename__ = 'data'
	id = Column(Integer, primary_key=True)	
	carousel_pic = Column(String)
	carousel_title = Column(String)
	carousel_text = Column(String)
