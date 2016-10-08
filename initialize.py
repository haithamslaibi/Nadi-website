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


admin = Admin (username = 'admin' ,password = 'admin')
#test_data = Data()

session.add(admin)

session.commit()

print("Congratz you have a new db")








