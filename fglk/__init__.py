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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/banner_data')
def banner_data():
    data = [
        {'img-link': 'https://wallpapers.com/images/high/spider-man-action-adventure-1080p-gaming-6psueyj01802y9f1.webp', 'text': 'Text 1','heading':'this is 1 heding','button-link':'https://www.youtube.com/watch?v=Tkgad9gngOQ&list=TLPQMjkwMzIwMjR-4Q5iotF2uQ','button-text':'YO Yo Song -1'},
        {'img-link': 'https://wallpapers.com/images/high/pubg-squad-season-17-runic-power-ro0lxrrstvdsl6jo.webp', 'text': 'Text 2','heading':'this is 2 heding','button-link':'https://www.youtube.com/watch?v=nCD2hj6zJEc','button-text':'YO Yo Song -2'},
        {'img-link': 'https://wallpapers.com/images/high/victor-in-winter-pubg-1366x768-35gglmh40a6i8jl2.webp', 'text': 'Text 3','heading':'this is 3 heding','button-link':'https://www.youtube.com/watch?v=nCD2hj6zJEc','button-text':'Hot '}
    ]
    return jsonify(data)
@app.route('/2')
def index2():
    return render_template('index2.html')
@app.route('/sample')
def sample():
    return jsonify({'message':'tet'})

@app.route('/about')
def about():
    return 'about page'



