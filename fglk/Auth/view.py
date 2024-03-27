from flask import Blueprint,redirect,flash,render_template,url_for,request,session
from fglk import app
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,login_user,login_required,current_user,logout_user
from fglk.Auth.form import LoginForm, RegistrationForm, RegistrationFormadmin,ForgotPasswordForm,OtpForm,ResetPasswordForm
from secrets import token_hex
from fglk.database import db
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from fglk.Auth.modles import Student, Admin
from config import Config
from .Mail import SendMail
from .Otp import generate_otp,check_otp
## can use flask cache memory to store the memeory into flask carche ##

Auth=Blueprint('Auth',__name__,template_folder='templates/Auth',static_folder='static')

bcrypt = Bcrypt(app)
login_manager=LoginManager(app)


      
@login_manager.user_loader
def load_user(user_id):
    # Assuming you have a way to retrieve the user from the user ID
    user_data = db.users.find_one({'_id': ObjectId(user_id)})
    if user_data:
        if user_data['role'] =='Student':
            return Student(user_data['_id'], user_data['name'],user_data['role'],user_data['courses'],user_data['email'],user_data['token'])
        elif user_data['role']=='Admin':
            return Admin(user_data['_id'],user_data['name'],user_data['email'],user_data['role'],user_data['token'])
    return None


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')

@Auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_data = db.users.find_one({'email': form.email.data})
        if user_data and bcrypt.check_password_hash(user_data['password'], form.password.data):
            if user_data['role'] =='Student':
                user= Student(user_data['_id'], user_data['name'],user_data['role'],user_data['courses'],user_data['email'],user_data['token'])
            elif user_data['role']=='Admin':
                user= Admin(user_data['_id'],user_data['name'],user_data['email'],user_data['role'],user_data['token'])   
            token = token_hex(16)  # Generate a 32-character random token
            db.users.update_one({'_id': user.user_id}, {'$set': {'token': token}})
            login_user(user)
            if user_data['role'] == 'Admin':
                response = redirect(url_for("Admin.AdminIndex"))###--- this also change
                response.set_cookie('token', token)
                return response
            elif user_data['role'] == 'Student':
                response = redirect(url_for("Auth.test_login"))###--- this also change
                response.set_cookie('token', token)
                return response
        else:
            flash('Invalid username or password!', 'error')
    return render_template('login.html', form=form)


@Auth.route('/register', methods=['GET', 'POST'])
def register():
    role = request.args.get('role')  # Check if 'role' parameter is provided in the URL
    collection = db['users']
    if role == 'admin':
        form = RegistrationFormadmin()
    else:
        form = RegistrationForm()
    
    if form.validate_on_submit():
        if db.users.find_one({'email': form.email.data}):
            flash('Email already exists!', 'error')
        else:
            date = datetime.now()
            password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            data = {'email': form.email.data,
                    'password': password_hash,
                    'name': form.name.data,
                    'role': 'Admin' if role == 'admin' else 'Student',
                    'token': None,
                    'date_of_register': date,
                    }
            if role != 'admin':
                data['courses']=None
            if role == 'admin' and Config.ADMINKEY != form.adminkey.data:
                flash('Key is incorrect', 'error')
            else:
                collection.insert_one(data)
                flash('Registration successful! You can now login.', 'success')
                return redirect('/login')
    
    return render_template('register.html', form=form, role=role)




@Auth.route('/forgot_password' , methods=['GET', 'POST'])
def forgot_password():
    form=ForgotPasswordForm()
    if form.validate_on_submit():
        email=form.email.data
        userX=db.users.find_one({'email':email})
        if userX:
            session['email']=email
            session['otp_bycrypt']=generate_otp(email,6)
            return redirect (url_for('Auth.otp'))
        flash('Not user', 'error')
        return render_template('forgot_password.html',form=form)
        # return session.get('email')
    return render_template('forgot_password.html',form=form)

@Auth.route('/otp', methods=['GET', 'POST'])
def otp():
    if session.get('email') and session.get('otp_bycrypt') :
        form=OtpForm()
        if form.validate_on_submit():
            otp=form.otp.data
            if check_otp(otp,session.get('otp_bycrypt')):
                return redirect (url_for('Auth.reset_password'))
            else:
                flash('Invalid Otp!', 'error')
                return render_template('otp.html',form=form)
        return render_template('otp.html',form=form)
    else:
        return redirect (url_for('Auth.forgot_password'))


@Auth.route('/resetPassword', methods=['GET', 'POST'])
def reset_password():
    if not session.get('email'):
        return redirect (url_for('Auth.login'))
    form=ResetPasswordForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.users.update_one({'email': session.get('email')}, {'$set': {'password': password_hash}})
        session.pop('email',None)
        session.pop('otp_bycrypt',None)
        return redirect(url_for('Auth.login'))
    return render_template('resetPassword.html',form=form)



@login_required
@Auth.route('/test')
def test_login():
    token = request.cookies.get('token')
    return {'token':token,'id':str(current_user.user_id),'name':str(current_user.name),'role':str(current_user.role)}

@Auth.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@Auth.route('/logout')
@login_required
def logout():
    db.users.update_one({'_id': current_user.user_id}, {'$set': {'token': None}})
    logout_user()
    response = redirect(url_for('Auth.login'))
    response.delete_cookie('token')  # Remove the token cookie
    return response