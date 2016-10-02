from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import *
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
	horse_lists = []
	List = session.query(Horses).all()
	for i in range(0, len(List), 4):
		sub_list = List[i:i + 4]
		horse_lists.append(sub_list)
	return render_template('Horses.html' , horse_lists = horse_lists)


@app.route('/Riders')
def riders():
	rider_lists = []
	List = session.query(Users).all()
	for i in range(0, len(List), 4):
		sub_list = List[i:i + 4]
		rider_lists.append(sub_list)
	return render_template('Riders.html' , rider_lists = rider_lists)


@app.route('/Score')
def score():
	rider_list = session.query(Users).all()
	return render_template('Score.html' , rider_list = rider_list)


@app.route('/Admin',methods = ['GET', 'POST'])
def admin():
	if request.method == 'POST':
		username = session.query(Admin).filter_by(username = request.form['username']).first()
		if username == None or username.password != request.form['password']:
			print ("Wrong")
			return render_template('Admin.html', error=True)
		else:  
			return render_template('Admin_Home.html')
	else:
		return render_template('Admin.html')



if __name__ == '__main__':
    app.run(debug=True)
