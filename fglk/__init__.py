from dotenv import load_dotenv
from flask import Flask, jsonify,render_template
from config import Config


load_dotenv(override=True)

app = Flask(__name__)
app.config.from_object(Config)

from fglk.Auth.view import Auth
app.register_blueprint(Auth,url_prefix='/')

from fglk.Admin.view import Admin
app.register_blueprint(Admin,url_prefix='/admin')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/2')
def index2():
    return render_template('index2.html')
@app.route('/sample')
def sample():
    return jsonify({'message':'tet'})

@app.route('/about')
def about():
    return 'about page'



