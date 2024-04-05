from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId

# /com is the url
Admin_Community = Blueprint('Admin_Community',
                            __name__,
                            template_folder='templates/Admin_Community',
                            static_folder='static')

@Admin_Community.route('/')
def asd():
    return 'asd'