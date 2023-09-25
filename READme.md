# PIZZAS RESTAURANT

by Christine K Juma.

  ## DESCRIPTION

Welcome to the Pizza Restaurant API! This Flask application serves as the backend for managing a pizza restaurant, allowing users to interact with

restaurants, pizzas, and their relationships. Follow the instructions below to set up and use the API.

  ## REQUIREMENTS

Ensure that you have;

1. A computer. 

2. Python installed.

 ## TECHNOLOGY USED

 - Python.

 - SQLAlchemy

 - Flask

 - SQLite

 - Flask-migrate

  ## MODELS AND DATABASE RELATIONSHIPS

This application follows the following database relationships:

- A Restaurant has many Pizzas through RestaurantPizza.

- A Pizza has many Restaurants through RestaurantPizza.

- A RestaurantPizza belongs to a Restaurant and belongs to a Pizza.

  ## VALIDATIONS

1. RestaurantPizza:

- Price must be between 1 and 30.

2. Restaurant:

- Name must be less than 50 characters.

- Name must be unique.

  ## RUNNING THE PROJECT

1. Clone the repository to your local machine. 

   ```bash
   git clone <repository>
   ``` 

2. Start the Flask application.

   ```bash
    flask run   
   ```

3. The application will be accessible at http://localhost:5000.   

## LICENSE

MIT License

Copyright (c) 2023 Christine K Juma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## AUTHOR

This project's aurthor is;

  Christine K Juma

[Click Here for Github Link](https://github.com/christine-M9)
