from myproject import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False, unique=True)  # Make phone number unique
    password_hash = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)

    def __init__(self, first_name, last_name, phone_no, password, state, pincode):
        self.first_name = first_name 
        self.last_name = last_name
        self.phone_no = phone_no
        self.password_hash = generate_password_hash(password)
        self.state = state
        self.pincode = pincode
    
    def check_password(self, password):
        """
        Checks if the given password matches the stored hash.
        """
        return check_password_hash(self.password_hash, password)

    def create_access_token(self):
        """
        Creates a JWT access token for the user.
        """
        return create_access_token(identity=self.id)

    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name}, State : {self.state}"
