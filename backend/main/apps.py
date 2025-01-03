from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulate a simple in-memory database with a dictionary
users = {
    1: {"name": "John Doe", "email": "john@example.com"},
    2: {"name": "Jane Smith", "email": "jane@example.com"}
}

# Get all users (Read operation)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get a single user by ID (Read operation)
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Create a new user (Create operation)
@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()  # Get JSON data from the request
    user_id = max(users.keys()) + 1  # Generate new ID (simple approach)
    users[user_id] = new_user
    return jsonify(new_user), 201  # Respond with the created user

# Update an existing user (Update operation)
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if user:
        updated_user = request.get_json()  # Get updated data
        users[user_id] = updated_user
        return jsonify(updated_user)
    else:
        return jsonify({"error": "User not found"}), 404

# Delete a user (Delete operation)
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)  # Remove user by ID
    if user:
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
