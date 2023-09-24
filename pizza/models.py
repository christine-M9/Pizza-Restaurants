from app import db

class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', backref='restaurants')

    def __init__(self, name, address):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        self.name = name
        self.address = address

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(100), nullable=False)

class RestaurantPizza(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def __init__(self, price, restaurant_id, pizza_id):
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30")
        self.price = price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id
