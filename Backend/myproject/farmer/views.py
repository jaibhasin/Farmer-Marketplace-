from flask import Flask, render_template, redirect, url_for, Blueprint, request, jsonify
from myproject import db
from myproject.farmer.models import Farmer, Crops
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

farmer_bp = Blueprint('farmer_bp', __name__)

# JWTManager already initialized in __init__.py

@farmer_bp.route('/sign-up/', methods=['POST'])
def sign_up():
    data = request.json

    first_name = data.get('fname')
    last_name = data.get('lname')
    phone_no = data.get('phone')
    password_h = data.get('password')
    state = data.get('state')
    pincode = data.get('pincode')

    if not first_name or not last_name or not password_h:
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400

    # Check if phone number already exists
    existing_farmer = Farmer.query.filter_by(phone_no=phone_no).first()
    if existing_farmer:
        return jsonify({'success': False, 'error': 'Farmer with this phone number already exists'}), 400

    # Create a new Farmer object
    new_farmer = Farmer(first_name=first_name, last_name=last_name, phone_no=phone_no, password=password_h, state=state, pincode=pincode)
    db.session.add(new_farmer)
    db.session.commit()

    # Generate JWT Token
    access_token = create_access_token(identity=phone_no)

    return jsonify({"success": True, "message": "Farmer created successfully!", "access_token": access_token}), 201


@farmer_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    phone_no = data.get('phone')
    password = data.get('password')

    if not phone_no or not password:
        return jsonify({'error': 'Phone number and password are required'}), 400

    # Query the Farmer by phone number
    farmer = Farmer.query.filter_by(phone_no=phone_no).first()

    if farmer is None or not farmer.check_password(password):
        return jsonify({'error': 'Invalid phone number or password'}), 401

    # Generate JWT Token
    access_token = create_access_token(identity=phone_no)

    return jsonify({'success': True, 'access_token': access_token}), 200


@farmer_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({'message': 'Successfully logged out, but the token is invalidated on client side.'}), 200


@farmer_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user_phone = get_jwt_identity()

    # Query the Farmer by phone number
    farmer = Farmer.query.filter_by(phone_no=current_user_phone).first()

    if not farmer:
        return jsonify({'error': 'Farmer not found'}), 404

    return jsonify({'message': f'Welcome, {farmer.first_name} {farmer.last_name}! This is your dashboard.'}), 200


@farmer_bp.route('/add-crop/', methods=['POST'])
@jwt_required()
def add_crop():
    data = request.json

    crop = data.get('crop')
    quantity = data.get('quantity')
    date = data.get('date')
    price = data.get('price')

    if not crop or not quantity or not date or not price:
        return jsonify({'error': 'Missing required fields'}), 400

    current_user_phone = get_jwt_identity()

    # Create a new Crops object using the current user's phone number
    new_crop = Crops(crop=crop, quantity=quantity, date=date, price=price, phone_no=current_user_phone)
    db.session.add(new_crop)
    db.session.commit()

    return jsonify({'message': 'Crop added successfully!'}), 201


@farmer_bp.route('/list-crops/', methods=['GET'])
@jwt_required()
def list_crops():
    current_user_phone = get_jwt_identity()

    # Query all crops for the current user
    crops = Crops.query.filter_by(phone_no=current_user_phone).all()
    crops_list = [{'crop': crop.crop, 'quantity': crop.quantity, 'date': crop.date, 'price': crop.price} for crop in crops]

    return jsonify(crops_list), 200
