from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64), index=True)

    def __init__(self, id, customer_name):
        self.id = id
        self.customer_name = customer_name
