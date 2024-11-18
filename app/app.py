from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS  

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

CORS(app)

data_store = []  # Una semplice lista per tenere i dati utente
users = {}  # Un dizionario per memorizzare utenti e password

# Endpoint per la pagina HTML
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint per registrare un nuovo utente
# Pagina di registrazione
@app.route('/auth/register', methods=['POST'])
def register():
     # Ricezione dei dati in formato JSON
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    # Verifica degli input
    if not email or not password:
        return jsonify({'error': 'Invalid input'}), 400

    # Verifica se l'utente esiste già
    if email in users:
        return jsonify({'error': 'User already exists'}), 400

    # Registrazione dell'utente
    users[email] = password

    # Creazione di un token JWT per il nuovo utente
    access_token = create_access_token(identity=email)
    
    # Restituzione di una risposta di successo con il token JWT
    return jsonify(access_token=access_token, message="User registered successfully"), 201


# Endpoint per autenticare un utente
@app.route('/auth/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    
    if email in users and users[email] == password:
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'error': 'Authentication failed'}), 401
    

# Pagina per il logout
@app.route('/auth/logout', methods=['GET'])
def logout():
     return jsonify({"message": "User logged out successfully"}), 200


@app.route('/auth/reset-password', methods=['POST'])
def reset_password():
    email = request.json.get('email', None)

    if not email:
        return jsonify({'error': 'Invalid input'}), 400

    if email not in users:
        return jsonify({'error': 'User not found'}), 404

    # Qui simuleremo l'invio dell'email di reset della password
    # In un contesto reale, si potrebbe inviare un'email con un link di reset
    return jsonify({'message': 'Password reset email sent'}), 200

# Pagina principale simile a Netflix
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000, debug=True)
