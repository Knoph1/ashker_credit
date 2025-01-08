# Directory: backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access the HEROKU_API_KEY
heroku_api_key = os.getenv('HEROKU_API_KEY')

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Firebase Initialization
cred = credentials.Certificate(os.getenv("FIREBASE_SERVICE_ACCOUNT"))
firebase_admin.initialize_app(cred)
db = firestore.client()
products_ref = db.collection('products')
orders_ref = db.collection('orders')

@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all products."""
    products = [doc.to_dict() for doc in products_ref.stream()]
    return jsonify(products), 200

@app.route('/order', methods=['POST'])
def create_order():
    """Create a new order."""
    data = request.json
    orders_ref.add(data)
    return jsonify({"success": True, "message": "Order created successfully"}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    """Fetch all orders."""
    orders = [doc.to_dict() for doc in orders_ref.stream()]
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(debug=True)
