from dotenv import load_dotenv
from flask import Flask, jsonify,render_template
from config import Config
from flask_cors import CORS


load_dotenv(override=True)

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

from fglk.Auth.view import Auth
app.register_blueprint(Auth,url_prefix='/')

from fglk.Admin.view import Admin
app.register_blueprint(Admin,url_prefix='/admin')

from fglk.Student.view import Student
app.register_blueprint(Student,url_prefix='/student')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/banner_data')
def banner_data():
    data = [
        {'tags':['#law-kida','#awe','#Raja','#LadyLove'],'img-link': 'https://wallpapers.com/images/high/spider-man-action-adventure-1080p-gaming-6psueyj01802y9f1.webp', 'text': 'Animals, diverse in shape and behavior, inhabit ecosystems worldwide, contributing to biodiversity, ecosystems, and human well-being through various roles and interactions.','heading':'Lorem ipsum dolor sit','button-link2':'https://www.youtube.com/watch?v=Tkgad9gngOQ&list=TLPQMjkwMzIwMjR-4Q5iotF2uQ','button-text':'Button 1'},
        {'tags':['#jan','#feb','#till','#king'],'img-link': 'https://wallpapers.com/images/high/pubg-squad-season-17-runic-power-ro0lxrrstvdsl6jo.webp', 'text': 'Cars revolutionized transportation, offering convenience, speed, and freedom. They vary in design, features, and performance, shaping modern lifestyles globally.','heading':'which can change automatically.','button-link2':'https://www.youtube.com/watch?v=nCD2hj6zJEc','button-text':'Button 2'},
        {'tags':['#me','#you','#it','#us','#parth Jain',"#fake Law"],'img-link': 'https://wallpapers.com/images/high/victor-in-winter-pubg-1366x768-35gglmh40a6i8jl2.webp', 'text': 'Bikes, versatile vehicles, offer efficient transportation, promoting exercise and reducing emissions, enhancing urban mobility and personal health.','heading':'This is a banner ','button-link2':'https://youtu.be/8Z8qobg8UdA?si=MWJtXivbR6UJfs_J','button-text':'Button 3'}
    ]
    return jsonify(data)

@app.route('/sample')
def sample():
    return jsonify({'message':'tet'})

@app.route('/about')
def about():
    return 'about page'

@app.route('/card')
def card():
    return render_template('card.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/otp')
def otp():
    return render_template('otp.html')

@app.route('/resetPassword')
def resetPassword():
    return render_template('resetPassword.html')