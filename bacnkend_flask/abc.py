from myproject import app, db
from myproject.farmer.models import Farmer

with app.app_context():
    farmers = Farmer.query.all()
    for farmer in farmers:
        print(farmer)