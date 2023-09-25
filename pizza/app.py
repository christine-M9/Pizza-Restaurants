from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import models
from models import Restaurant, Pizza, RestaurantPizza

# Home route
@app.route('/')
def index():
    return 'HELLO, WELCOME TO CHRISTINES PIZZA RESTAURANTS!'

# Route to get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_info = [{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants]
    return jsonify(restaurant_info)

# Route to get a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizza_data = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        restaurant_info = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': pizza_data
        }
        return jsonify(restaurant_info)
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

# Route to get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_info = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas]
    return jsonify(pizza_info)     

# Route to create a new Pizza
@app.route('/pizzas', methods=['POST'])
def create_pizza():
    info = request.json
    name = info.get('name')
    ingredients = info.get('ingredients')
    
    if name is None or ingredients is None:
        return jsonify({'errors': ['validation errors']}), 400

    pizza = Pizza(name=name, ingredients=ingredients)
    db.session.add(pizza)
    db.session.commit()

    return jsonify({
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }), 201

# Route to create a new Restaurant
@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    info = request.json
    name = info.get('name')
    address = info.get('address')
    
    if name is None or address is None:
        return jsonify({'errors': ['validation errors']}), 400

    restaurant = Restaurant(name=name, address=address)
    db.session.add(restaurant)
    db.session.commit()

    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address
    }), 201

# Delete a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        # Delete associated RestaurantPizzas first
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

# Route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    info = request.json
    price = info.get('price')
    pizza_id = info.get('pizza_id')
    restaurant_id = info.get('restaurant_id')
    
 # Validating inputs
    if price is None or pizza_id is None or restaurant_id is None:
        print("Validation error")
        return jsonify({'errors': ['validation errors']}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if pizza is None or restaurant is None:
        print("Pizza or restaurant not found")
        return jsonify({'errors': ['validation errors']}), 400

    restaurant_pizza = RestaurantPizza(price=price, restaurant_id=restaurant_id, pizza_id=pizza_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    #print("Successfully created restaurant pizza")

    return jsonify({
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }), 201



# Route to get all restaurant_pizzas
@app.route('/restaurant_pizzas', methods=['GET'])
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    restaurant_pizza_info = [{
        'id': rp.id,
        'price': rp.price,
        'restaurant_id': rp.restaurant_id,
        'pizza_id': rp.pizza_id
    } for rp in restaurant_pizzas]
    return jsonify(restaurant_pizza_info)



if __name__ == '__main__':
    app.run(debug=True)
