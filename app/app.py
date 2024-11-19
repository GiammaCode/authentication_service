from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Secret key for signing JWT tokens
jwt = JWTManager(app)

CORS(app)  # Enable Cross-Origin Resource Sharing to allow requests from other origins

data_store = []  # to store user data

# View all users
@app.route('/auth/users', methods=['GET'])
def view_all_users():
    # Return all users without passwords for security purposes
    user_list = [{"email": user["email"]} for user in data_store]
    return jsonify(user_list), 200

# Endpoint to register a new user
@app.route('/auth/register', methods=['POST'])
def register():
    """
    Register a new user by receiving email and password in JSON format.
    If the user does not already exist, create the user and return a JWT access token.
    """
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email or not password:
        return jsonify({'error': 'Invalid input'}), 400
    if any(user["email"] == email for user in data_store):
        return jsonify({'error': 'User already exists'}), 400

    # Add new user to data_store
    new_user = {"email": email, "password": password}
    data_store.append(new_user)

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token, message="User registered successfully"), 201

# Endpoint for authenticating a user
@app.route('/auth/login', methods=['POST'])
def login():
    """
    Authenticate an existing user.
    If the email and password are correct, return a JWT access token.
    """
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    
    # Find the user in data_store
    user = next((user for user in data_store if user["email"] == email and user["password"] == password), None)
    
    if user:
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Authentication failed'}), 401

# Endpoint for logging out a user
@app.route('/auth/logout', methods=['GET'])
def logout():
    """
    Logout endpoint.
    In a real scenario, this might include invalidating the user's token.
    """
    return jsonify({"message": "User logged out successfully"}), 200

# Endpoint for resetting a user's password
@app.route('/auth/reset-password', methods=['POST'])
def reset_password():
    """
    Reset the user's password by receiving the email in JSON format.
    If the user exists, simulate sending a reset password email.
    """
    email = request.json.get('email', None)

    if not email:
        return jsonify({'error': 'Invalid input'}), 400
    if not any(user["email"] == email for user in data_store):
        return jsonify({'error': 'User not found'}), 404
    
    # Simulate sending a reset email
    return jsonify({'message': 'Password reset email sent'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)