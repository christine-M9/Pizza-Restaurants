from app import db

# Defining a Restaurant class that inherits from db.Model
class Restaurant(db.Model):

# Attributes/columns for the Restaurant table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)

# Creating a relationship with the Pizza table using the secondary table 'restaurant_pizza'
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', backref='restaurants')

# Initializing a Restaurant object
    def __init__(self, name, address):
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
        self.name = name
        self.address = address

# Defining a Pizza class that inherits from db.Model
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(100), nullable=False)

# Defining a RestaurantPizza class that inherits from db.Model
class RestaurantPizza(db.Model):

# Attributes/columns for the RestaurantPizza table
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

# Defining foreign keys to associate with Restaurant and Pizza tables    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

 # Initializing a RestaurantPizza object
    def __init__(self, price, restaurant_id, pizza_id):

 # Checking if the price is between 1 and 30       
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30")
        self.price = price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id
