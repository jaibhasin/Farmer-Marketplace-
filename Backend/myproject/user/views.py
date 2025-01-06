from flask import Flask, render_template, redirect, url_for, Blueprint, request, jsonify
from myproject import db
from myproject.user.models import User
from myproject.farmer.models import Farmer, Crops
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Blueprint
user_bp = Blueprint('user_bp', __name__)

# Setup JWT Manager
jwt = JWTManager()

@user_bp.route('/sign-up/', methods=['POST'])
def sign_up():
    """
    User Registration Route
    """
    data = request.json  # For JSON input
    first_name = data.get('fname')
    last_name = data.get('lname')
    phone_no = data.get('phone')
    password_h = data.get('password')
    state = data.get('state')
    pincode = data.get('pincode')

    # Check for missing fields
    if not first_name or not last_name or not password_h:
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400

    # Check if phone number already exists
    if User.query.filter_by(phone_no=phone_no).first():
        return jsonify({'success': False, 'error': 'Phone number already exists'}), 400

    # Create a new User object
    new_user = User(first_name=first_name, last_name=last_name, phone_no=phone_no, password=password_h, state=state, pincode=pincode)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201


@user_bp.route('/login', methods=['POST'])
def login():
    """
    User Login Route
    """
    data = request.json  # Assuming JSON input from Postman

    phone_no = data.get('phone')
    password = data.get('password')

    if not phone_no or not password:
        return jsonify({'error': 'Phone number and password are required'}), 400

    # Query the User by phone number
    user = User.query.filter_by(phone_no=phone_no).first()

    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Check if the password is correct using the check_password method
    if not user.check_password(password):
        return jsonify({'success': False, 'error': 'Invalid password'}), 401

    # Create JWT token (expires in 1 hour)
    access_token = create_access_token(identity=user.id, fresh=True)

    return jsonify({
        'message': 'Login successful!',
        'access_token': access_token
    }), 200


@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """
    User Logout Route
    (Optional, depending on how you handle JWT expiration or invalidation)
    """
    return jsonify({'message': 'User logged out successfully!'}), 200

@user_bp.route('/crop-listings/', methods=['POST', 'GET'])
@jwt_required()
def crop_listings():
    """
    Crop Listings Route
    This route is protected by JWT authentication, only accessible by authenticated users.
    """
    current_user_id = get_jwt_identity()  # Get the user ID from the JWT

    data = request.json
    print("Received Data:", data)  # Log the data received
    crop_name = data.get('crop')
    quantity = data.get('quantity')

    if not crop_name or quantity is None:
        return jsonify({'error': 'Crop name and quantity are required'}), 400

    # Query the Farmer's crops based on the crop name and quantity
    crops = Crops.query.join(Farmer).filter(Crops.crop == crop_name, Crops.quantity >= quantity).all()

    # Create the result list to return the necessary details
    result = [{'farmer_first_name': crop.farmer.first_name, 'farmer_last_name': crop.farmer.last_name, 
               'crop_name': crop.crop, 'quantity': crop.quantity, 'price': crop.price, 'State': crop.farmer.state} for crop in crops]

    return jsonify(result), 200
