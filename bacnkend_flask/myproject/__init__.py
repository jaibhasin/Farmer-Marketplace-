import os
from flask import Flask , render_template , url_for , redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_login import LoginManager, login_required


load_dotenv()

app = Flask(__name__)


app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'None'  # Allow cross-domain cookies
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookies are only sent over HTTPS (if you're deploying over HTTPS)


db = SQLAlchemy(app)

Migrate(app,db)

from myproject.ml_model import predict_crop, get_user_input
from myproject.final_model_fertlizer import user_input
@app.route('/get_crop', methods=['POST'])
def get_crop():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        user_input = get_user_input(
            data['n'],
            data['p'],
            data['k'],
            data['temperature'],
            data['humidity'],
            data['ph'],
            data['rainfall']
        )
    except KeyError as e:
        return jsonify({"error": f"Missing parameter: {str(e)}"}), 400

    prediction = predict_crop(user_input)
    print(prediction)
    return jsonify({"prediction": prediction})

@app.route('/')
def index():
    return "This is index page"

@app.route('/get_fertilizer', methods=['POST'])
def get_fertilizer():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        n = data['n']
        p = data['p']
        k = data['k']
        crop_type = data['crop']
    except KeyError as e:
        return jsonify({"error": f"Missing parameter: {str(e)}"}), 400

    result = user_input(n, p, k, crop_type)
    # print("hi")
    return jsonify({"result": result})

login_manager = LoginManager()
login_manager.init_app(app)

from myproject.farmer.views import farmer_bp
app.register_blueprint(farmer_bp, url_prefix='/farmer')
login_manager.login_view = "farmer_bp.login"

# import user views
from myproject.user.views import user_bp
app.register_blueprint(user_bp, url_prefix='/user')
# login_manager.login_view = "user_bp.login"
