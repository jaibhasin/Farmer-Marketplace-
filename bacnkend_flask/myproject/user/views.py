from flask import Flask , render_template , redirect , url_for, Blueprint, request , jsonify
from myproject import db   
from myproject.user.models import User
from myproject.farmer.models import Farmer, Crops
from flask_login import login_user, logout_user, login_required, current_user


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/sign-up/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return "Sign-Up page is accessible only via POST for creating a new User."

    data = request.json  # For JSON input
    # data = request.form  # For form-encoded input
    first_name = data.get('fname')
    last_name = data.get('lname')
    phone_no = data.get('phone')
    password_h = data.get('password')
    state = data.get('state')
    pincode = data.get('pincode')
    # Check for missing fields
    if not first_name or not last_name  or not password_h:
        return jsonify({'success':False,'error': 'Missing required fields'}), 400

    # Create a new Farmer object
    new_user = User(first_name=first_name , last_name=last_name , phone_no=phone_no , password=password_h , state=state , pincode=pincode)  # Adjust based on your Farmer model
    db.session.add(new_user)
    login_user(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201



@user_bp.route('/login', methods=['POST' , 'GET'])
def login():
    if request.method == 'GET':
        return "Login page is accessible only via POST for loggin in  a user."
    

    data = request.json  # Assuming JSON input from Postman

    phone_no = data.get('phone')
    password = data.get('password')

    if not phone_no or not password:
        return jsonify({'error': 'Phone number and password are required'}), 400

    # Query the Farmer by phone number
    user = User.query.filter_by(phone_no=phone_no).first()

    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Check if the password is correct using the check_password method
    if not user.check_password(password):
        return jsonify({'success':False,'error': 'Invalid password'}), 401

    # Log the user in
    login_user(user)

    return jsonify({'success': True}), 200


@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user_bp.login'))

@user_bp.route('/crop-listings/', methods=['POST', 'GET'])
# @login_required
def crop_listings():
    if request.method == 'GET':
        return "Listings page is accessible only via POST for viewing crop listings."
    print(current_user.first_name)
    data = request.json
    crop_name = data.get('crop')
    quantity = data.get('quantity')

    if not crop_name or quantity is None:
        return jsonify({'error': 'Crop name and quantity are required'}), 400

    # Query the Farmer's crops based on the crop name and quantity
    crops = Crops.query.join(Farmer).filter(Crops.crop == crop_name, Crops.quantity >= quantity).all()
 
    # Create the result list to return the necessary details
    result = [{'farmer_first_name': crop.farmer.first_name, 'farmer_last_name': crop.farmer.last_name, 
               'crop_name': crop.crop, 'quantity': crop.quantity, 'price': crop.price , 'State':crop.farmer.state} for crop in crops]
    
    return jsonify(result), 200

