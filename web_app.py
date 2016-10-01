from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Horses')
def horses():
	return render_template('Horses.html')

@app.route('/Riders')
def riders():
	return render_template('Riders.html')

@app.route('/Score')
def score():
	return render_template('Score.html')



if __name__ == '__main__':
    app.run(debug=True)
