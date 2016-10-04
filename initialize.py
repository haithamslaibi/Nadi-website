from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *
from datetime import datetime

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.


session.query(Users).delete()
session.query(Horses).delete()
session.query(Data).delete()


haitham = Users(name='Haitham Slaibi',birthday = datetime(year=1997,month=5,day=13), password = 'test' , score = 20 , username = 'haitham.slaibi' , slogan = 'best' ,course_height = 120 , pic = 'none')
raneem =Users(name='Raneem Slaibi',birthday = datetime(year=2000,month=1,day=16), password = 'test' , score = 10 , username = 'raneem.slaibi' , slogan = 'habla' ,course_height = 100 , pic = 'none')


test_horse1 = Horses(name = 'Layali' , birthday = datetime(year=2001,month=5,day=13), height = 160 ,max_jump = 150 , course_height = 120 , pic='none' ,owner = 'me')
test_horse2 = Horses(name = 'palestine' , birthday = datetime(year=2001,month=5,day=13), height = 160 , max_jump = 150 , course_height = 120 , pic='none',owner = 'me')
test_horse3 = Horses(name = 'bahar' , birthday = datetime(year=2001,month=5,day=13), height = 160 , max_jump = 150 , course_height = 120 , pic='none',owner = 'me')
test_horse4 = Horses(name = 'majnonee' , birthday = datetime(year=2001,month=5,day=13), height = 160 , max_jump = 150 , course_height = 120 , pic='none',owner = 'me')
test_horse5 = Horses(name = 'zain' , birthday = datetime(year=2001,month=5,day=13), height = 160 , max_jump = 150 , course_height = 120 , pic='none',owner = 'me')

admin = Admin (username = 'admin' ,password = 'admin')
#test_data = Data()

session.add(haitham)
session.add(raneem)

session.add(test_horse1)
session.add(test_horse2)
session.add(test_horse3)
session.add(test_horse4)
session.add(test_horse5)

session.add(admin)

session.commit()








