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


#My Imports
from datetime import *


#global variable
global temp
temp = False 


# helping functions


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



#############################################


@app.route('/')
def home():
	global temp    # singleton to make session_id = 0 
	if temp == False:
		session['user_id'] = 0 
		temp = True

	return render_template("Home.html" , id = session['user_id'])

@app.route('/Horses')
def horses():
	horse_lists = []
	List = dbsession.query(Horses).all()
	for i in range(0, len(List), 4):
		sub_list = List[i:i + 4]
		horse_lists.append(sub_list)
	return render_template('Horses.html' , horse_lists = horse_lists, id = session['user_id'])


@app.route('/Riders')
def riders():
	rider_lists = []
	List = dbsession.query(Users).all()
	for i in range(0, len(List), 4):
		sub_list = List[i:i + 4]
		rider_lists.append(sub_list)
	return render_template('Riders.html' , rider_lists = rider_lists, id = session['user_id'])


@app.route('/Profile/<int:user_id>')
def profile_anonymous(user_id):
	user = dbsession.query(Users).filter_by(id = user_id).first()
	return render_template ('Profile.html' , user = user, id = session['user_id'] ,age = calculate_age(dbsession.query(Users).filter_by(id = user_id).first().birthday))


@app.route('/Profile')
def profile():
	user = dbsession.query(Users).filter_by(id = session['user_id']).first()
	return render_template('Profile.html' ,id = session['user_id'], user = user , age = calculate_age(user.birthday))
	


@app.route('/LogOut')
def logOut():
	session['user_id'] = 0
	return redirect(url_for('home'))

@app.route('/Score')
def score():
	rider_list = dbsession.query(Users).all()
	return render_template('Score.html' , rider_list = rider_list , id = session['user_id'])

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


@app.route('/Horse_Profile/<int:horse_id>')
def horse_profile(horse_id):
	horse = dbsession.query(Horses).filter_by(id = horse_id).first()
	return render_template('Horse_Profile.html' , horse = horse)


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




@app.route('/Admin_Add' , methods = ['GET' , 'POST'])
def admin_add():

	if request.method == "POST":
		print("sdasdadsaaaaaaaaaaaaaaaaaaaaaaaa")			
		if request.form['carousel'] == 'carousel':
			print("carousel")
		elif request.form['rider'] == 'rider':
			riderbirthday = datetime(year =  int(request.form['year']) , month = int(request.form['month']),day = int(request.form['day']))
			
			rider = Users(name = request.form['ridername'],username = request.form['username'],
			password=request.form['password'],score = request.form['score'],
			birthday= riderbirthday ,horse = request.form['horsename'] , club = request.form['club'] ,
			pic = request.form['riderpic'] , slogan = request.form['slogan'] , course_height = request.form['ridercourseheight'],
			history = request.form['history'] )
			dbsession.add(rider)
			print("rider")
		elif request.form['horse'] == 'horse':
			horsebirthday = datetime(year =  int(request.form['hyear']) , month = int(request.form['hmonth']),day = int(request.form['hday']))

			horse = Horses(name = request.form['horsename'] , birthday = horsebirthday , max_jump = request.form['maxjump'] , pic = request.form['horsepic'] , owner=request.form['owner'] )

			dbsession.add(horse)
			print("horse")
		print("asssssssssssssssssssssssssssssssssssssssssssssss")
		dbsession.commit()
		
		return redirect(url_for('admin'))
	else :
		return redirect(url_for('home'))


# workinggg 
	if request.method == "POST":			
		riderbirthday = datetime(year =  int(request.form['year']) , month = int(request.form['month']),day = int(request.form['day']))
		
		rider = Users(name = request.form['ridername'],username = request.form['username'],
		password=request.form['password'],score = request.form['score'],
		birthday= riderbirthday ,horse = request.form['horsename'] , club = request.form['club'] ,
		pic = request.form['riderpic'] , slogan = request.form['slogan'] , course_height = request.form['ridercourseheight'],
		history = request.form['history'] )
		dbsession.add(rider)




		horsebirthday = datetime(year =  int(request.form['hyear']) , month = int(request.form['hmonth']),day = int(request.form['hday']))

		horse = Horses(name = request.form['horsename'] , birthday = horsebirthday , max_jump = request.form['maxjump'] , pic = request.form['horsepic'] , owner=request.form['owner'] )

		dbsession.add(horse)
		
		dbsession.commit()
		
		return redirect(url_for('admin'))
	else :
		return redirect(url_for('home'))








	# if request.method == "POST":
	# 	if request.form['ckeck'] == "carousel":
	# 		pass

	# 	elif request.form['check'] == "rider":			
			
	# 		birthday = datetime(year =  int(request.form['year']) , month = int(request.form['month']),day = int(request.form['day']))
			
	# 		rider = Users(name = request.form['ridername'],username = request.form['username'],
	# 		password=request.form['password'],score = request.form['score'],
	# 		birthday= birthday ,horse = request.form['horsename'] , club = request.form['club'] ,
	# 		pic = request.form['riderpic'] , slogan = request.form['slogan'] , course_height = request.form['ridercourseheight'],
	# 		history = request.form['history'] )
	# 		dbsession.add(rider)

	# 	elif request.form['check'] == "horse":
	
	# 		horse = Horses(name = request.form['horsename'],birthday = datetime(year=int(request.form['hyear']) ,
	# 		month = int(request.form['hmonth']) , day = int(request.form['hday']) ) , max_jump = request.form['maxjump'] ,
	# 		course_height = request.form['horsecourseheight'] , pic = request.form['horsepic'] , owner = request.form['owner']  )
			
	# 		dbsession.add(horse)
		
	# 	dbsession.commit()
		
	# 	return redirect(url_for('admin'))
	# else :
	# 	return redirect(url_for('home'))


@app.route('/Debug')
def debug(var1):
	return render_template('Debug.html' , var = var1)





if __name__ == '__main__':
	app.run(debug=True)
