# from myproject import db , login_manager
# from werkzeug.security import generate_password_hash , check_password_hash
# from flask_login import UserMixin


# @login_manager.user_loader
# def load_user(user_id):
# #     return User.query.get(phone_no=phone_number)
#     farmer = Farmer.query.get(id=user_id)
#     if farmer:
#         return farmer
    
#     # If not found in Farmer, try to get the user from the User model
#     user = User.query.get(phone_no = user_id)
#     if user:
#         return user
    
#     # If user is not found in either model, return None
#     return None




# # set login_manager 
# class Farmer(db.Model , UserMixin):
#     __tablename__ = 'farmers'  

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(100), nullable=False)
#     last_name = db.Column(db.String(100), nullable=False)
#     phone_no = db.Column(db.String(15), nullable=False) #set unique =True
#     password_hash = db.Column(db.String(128) , nullable=False)

#     state = db.Column(db.String(100), nullable=False)
#     pincode = db.Column(db.String(6), nullable=False)

#     def __init__(self , first_name , last_name , phone_no , password , state , pincode):
#         self.first_name = first_name 
#         self.last_name = last_name
#         self.phone_no = phone_no
#         self.password_hash = generate_password_hash(password)
#         self.state = state
#         self.pincode = pincode
    

#     def check_password(self,password):
#         # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
#         return check_password_hash(self.password_hash,password)

#     def __repr__(self):
#         return f"Name: {self.first_name} {self.last_name}, State : {self.state}"


# class Crops(db.Model):
#     __tablename__ = 'crops'  

#     id = db.Column(db.Integer, primary_key=True)
#     crop = db.Column(db.String(100), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     date = db.Column(db.String(255), nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#     phone_no = db.Column(db.String(15), db.ForeignKey('farmers.phone_no'), nullable=False)
#     farmer = db.relationship('Farmer', backref='crops', lazy=True)

#     def __init__(self, crop, quantity, date, price, phone_no):
#         self.crop = crop
#         self.quantity = quantity
#         self.date = date
#         self.price = price
#         self.phone_no = phone_no

#     def __repr__(self):
#         return f"Crop: {self.crop}, Quantity: {self.quantity}, Price: {self.price}"



# class User(db.Model ,UserMixin):
#     tablename = 'users'

#     id = db.Column(db.Integer)
#     first_name = db.Column(db.String(100), nullable=False)
#     last_name = db.Column(db.String(100), nullable=False)
#     phone_no = db.Column(db.String(15), nullable=False, primary_key=True) #set unique =True
#     password_hash = db.Column(db.String(128) , nullable=False)
#     state = db.Column(db.String(100), nullable=False)
#     pincode = db.Column(db.String(6), nullable=False)

#     def __init__(self , first_name , last_name , phone_no , password , state , pincode):
#         self.first_name = first_name 
#         self.last_name = last_name
#         self.phone_no = phone_no
#         self.password_hash = generate_password_hash(password)
#         self.state = state
#         self.pincode = pincode
    

#     def check_password(self,password):
#         return check_password_hash(self.password_hash,password)

#     def __repr__(self):
#         return f"Name: {self.first_name} {self.last_name}, State : {self.state}"
    
