from . import db



class vendingmachine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    stock = db.relationship('Stock', backref='vendingmachine', lazy=True)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255))
    vending_machine_id = db.Column(db.Integer, db.ForeignKey('vendingmachine.id'), nullable=False)

