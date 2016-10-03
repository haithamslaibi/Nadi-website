from flask import Flask, render_template,request, redirect, url_for , session
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

global temp
temp = False 

@app.route('/')
def home():
	global temp
	if temp == False:
		session['user_id'] = 0 
		temp = True

	if (session['user_id']) == 0 :
		return render_template("Home_Anonymus.html")
	else:
		return render_template("Home_User.html")

@app.route('/Horses')
def horses():
	horse_lists = []
	List = dbsession.query(Horses).all()
	for i in range(0, len(List), 4):
		sub_list = List[i:i + 4]
		horse_lists.append(sub_list)
	if (session['user_id']) == 0 :
		return render_template('Horses_Anonymus.html' , horse_lists = horse_lists)
	else:
		return render_template('Horses_User.html' , horse_lists = horse_lists)


@app.route('/Riders')
def riders():
	rider_lists = []
	List = dbsession.query(Users).all()
	for i in range(0, len(List), 4):
		sub_list = List[i:i + 4]
		rider_lists.append(sub_list)
	if (session['user_id']) == 0 :
		return render_template('Riders_Anonymus.html' , rider_lists = rider_lists)
	else:
		return render_template('Riders_User.html' , rider_lists = rider_lists)


@app.route('/Profile')
def profile():
	user = dbsession.query(Users).filter_by(id = session['user_id']).first()
	return render_template('Profile.html' , user = user)



@app.route('/LogOut')
def logOut():
	session['user_id'] = 0
	return redirect(url_for('home'))

@app.route('/Score')
def score():
	rider_list = dbsession.query(Users).all()
	if (session['user_id']) == 0 :
		return render_template('Score_Anonymus.html' , rider_list = rider_list)
	else:
		return render_template('Score_User.html' , rider_list = rider_list)
		
@app.route('/Admin',methods = ['GET', 'POST'])
def admin():
	if request.method == 'POST':
		username = dbsession.query(Admin).filter_by(username = request.form['username']).first()
		if username == None or username.password != request.form['password']:
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
		username = dbsession.query(Users).filter_by(username = request.form['username']).first()
		if username == None or username.password != request.form['password']:
			return render_template("Login.html" , error = True)
		else:
			session['user_id'] = username.id
			return redirect(url_for('home'))



@app.route('/Debug')
def debug(var1):
	return render_template('Debug.html' , var = var1)


if __name__ == '__main__':
	app.run(debug=True)
