from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)
app.secret_key = '43'

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import *
from sqlalchemy import create_engine ,or_
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
dbsession = DBSession()
session['user_id'] = -1

@app.route('/')
def home():
	if (session['user_id']) != None :
		print(session['user_id'])
	else:
		print("None")

	return render_template('Home.html')

@app.route('/Horses')
def horses():
	horse_lists = []
	List = dbsession.query(Horses).all()
	for i in range(0, len(List), 4):
		sub_list = List[i:i + 4]
		horse_lists.append(sub_list)
	return render_template('Horses.html' , horse_lists = horse_lists)


@app.route('/Riders')
def riders():
	rider_lists = []
	List = dbsession.query(Users).all()
	for i in range(0, len(List), 4):
		sub_list = List[i:i + 4]
		rider_lists.append(sub_list)
	return render_template('Riders.html' , rider_lists = rider_lists)


@app.route('/Score')
def score():
	rider_list = dbsession.query(Users).all()
	return render_template('Score.html' , rider_list = rider_list)


@app.route('/Admin',methods = ['GET', 'POST'])
def admin():
	if request.method == 'POST':
		username = dbsession.query(Admin).filter_by(username = request.form['username']).first()
		if username == None or username.password != request.form['password']:
			print ("Wrong")
			return render_template('Admin.html', error=True)
		else:  
			return render_template('Admin_Home.html')
	else:
		return render_template('Admin.html')



@app.route('/login',methods = ['GET' , 'POST'])
def login():
	if request.method == "GET":
		return render_template('Login.html')
	else:
		username = dbsession.query(Users).filter_by(name = request.form['username']).first()
		if username == None or username.password != request.form['password']:
			return render_template("Login.html" , error = True)
		else:
			session['user_id'] = username.id
			return redirect(url_for('home'))



if __name__ == '__main__':
	app.run(debug=True)
