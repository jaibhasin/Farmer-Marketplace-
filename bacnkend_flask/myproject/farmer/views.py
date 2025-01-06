from flask import Flask , render_template , redirect , url_for, Blueprint, request , jsonify
from myproject import db
from myproject.farmer.models import Farmer, Crops
from flask_login import login_user, logout_user, login_required, current_user

farmer_bp = Blueprint('farmer_bp' , __name__)

@farmer_bp.route('/sign-up/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return "Sign-Up page is accessible only via POST for creating a new farmer."


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
    new_farmer = Farmer(first_name=first_name , last_name=last_name , phone_no=phone_no , password=password_h , state=state , pincode=pincode)  # Adjust based on your Farmer model
    db.session.add(new_farmer)
    login_user(new_farmer)
    db.session.commit()

    return jsonify({"success":True,'message': 'Farmer created successfully!'}), 201

@farmer_bp.route('/login', methods=['POST' , 'GET'])
def login():
    if request.method == 'GET':
        return "Login page is accessible only via POST for creating a new farmer."


    data = request.json  # Assuming JSON input from Postman

    phone_no = data.get('phone')
    password = data.get('password')

    if not phone_no or not password:
        return jsonify({'error': 'Phone number and password are required'}), 400

    # Query the Farmer by phone number
    farmer = Farmer.query.filter_by(phone_no=phone_no).first()

    if farmer is None:
        return jsonify({'error': 'Farmer not found'}), 404

    # Check if the password is correct using the check_password method
    if not farmer.check_password(password):
        return jsonify({'success':False,'error': 'Invalid password'}), 401

    # Log the user in
    login_user(farmer)
    print(current_user.first_name)
    return jsonify({'success': True}), 200

    # Redirect to the dashboard with a success message
    # return redirect(url_for('farmer_bp.dashboard'))


@farmer_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('farmer_bp.login'))


@farmer_bp.route('/dashboard')
@login_required
def dashboard():
    return f"Welcome, {current_user.phone_no}! This is your dashboard."

@farmer_bp.route('/add-crop/', methods=['POST', 'GET'])
@login_required
def add_crop():
    if request.method == 'GET':
        return "Can be only created using post"
    data = request.json  # For JSON input
    crop = data.get('crop')
    quantity = data.get('quantity')
    date = data.get('date')
    price = data.get('price')

    if not crop or not quantity or not date or not price:
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a new Crops object using the current user's phone number
    new_crop = Crops(crop=crop, quantity=quantity, date=date, price=price, phone_no=current_user.phone_no)
    db.session.add(new_crop)
    db.session.commit()

    return jsonify({'message': 'Crop added successfully!'}), 201

@farmer_bp.route('/list-crops/', methods=['GET'])
@login_required
def list_crops():
    # Query all crops for the current user
    crops = Crops.query.filter_by(phone_no=current_user.phone_no).all()
    crops_list = [{'crop': crop.crop, 'quantity': crop.quantity, 'date': crop.date, 'price': crop.price} for crop in crops]

    return jsonify(crops_list), 200
