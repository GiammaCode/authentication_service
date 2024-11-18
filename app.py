from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

data_store = []  # Una semplice lista per tenere i dati utente
users = {}  # Un dizionario per memorizzare utenti e password

# Endpoint per la pagina HTML
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint per registrare un nuovo utente
@app.route('/auth/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({'error': 'Invalid input'}), 400

    if email in users:
        return jsonify({'error': 'User already exists'}), 400

    users[email] = password
    return jsonify({'message': 'User successfully registered'}), 201

# Endpoint per autenticare un utente
@app.route('/auth/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({'error': 'Invalid input'}), 400

    if users.get(email) == password:
        return jsonify({'accessToken': 'fake-jwt-token-for-' + email}), 200
    else:
        return jsonify({'error': 'Authentication failed'}), 401

# Endpoint per il logout di un utente
@app.route('/auth/logout', methods=['POST'])
def logout():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Invalid or expired token'}), 401

    # Per questo esempio, il logout viene simulato semplicemente con una risposta di successo
    return jsonify({'message': 'User logged out successfully'}), 200

# Endpoint per resettare la password di un utente
@app.route('/auth/reset-password', methods=['POST'])
def reset_password():
    email = request.form.get('email')

    if not email:
        return jsonify({'error': 'Invalid input'}), 400

    if email not in users:
        return jsonify({'error': 'User not found'}), 404

    # Per questo esempio, simuleremo l'invio dell'email di reset della password
    return jsonify({'message': 'Password reset email sent'}), 200

if __name__ == '__main__':
    app.run(debug=True)
