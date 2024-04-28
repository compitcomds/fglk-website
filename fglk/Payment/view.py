from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId
from datetime import datetime, timedelta

Payment = Blueprint('Payment',__name__,template_folder='templates/Payment',static_folder='static/Payment')

@Payment.before_request
@login_required
def checker():
      cookie_token = request.cookies.get('token')
      if current_user and current_user.token != cookie_token and ( current_user.role != 'Student') :
                flash('You have been logged out due to multiple logins.', 'error')
                return redirect(url_for('Auth.login'))
      elif current_user.role == 'Admin':
                return redirect(url_for('Admin.AdminIndex'))
      elif current_user.role == None:
              logout_user()
              return redirect (url_for('index'))
      
@Payment.route('/')
def index_Payment():
    data=db.course.find({})
    return render_template('payment.html',data=list(data))

@Payment.route('/<course_id>')
def make_payment(course_id):
        current_date = datetime.now()
        future_date = current_date + timedelta(days=40)
        db.users.update_one(
            {'_id': ObjectId(current_user.user_id)},
            {'$push': {
                'courses': {
                    'course_id': course_id,
                    'exp_date': future_date,
                    'purchase_date': current_date
                }
            }}
        )
        return redirect(url_for('Payment.index_Payment'))