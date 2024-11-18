from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

data_store = []  # Una semplice lista per tenere i dati utente
users = {}  # Un dizionario per memorizzare utenti e password

# Endpoint per la pagina HTML
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint per registrare un nuovo utente
# Pagina di registrazione
@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({'error': 'Invalid input'}), 400

        if email in users:
            return jsonify({'error': 'User already exists'}), 400

        users[email] = password
        return redirect(url_for('home'))

    return render_template('register.html')

# Endpoint per autenticare un utente
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({'error': 'Invalid input'}), 400

        if users.get(email) == password:
            return redirect(url_for('home'))
        else:
            return jsonify({'error': 'Authentication failed'}), 401

    return render_template('login.html')

# Pagina per il logout
@app.route('/auth/logout', methods=['GET'])
def logout():
    return redirect(url_for('index'))


# Endpoint per resettare la password di un utente
@app.route('/auth/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form.get('email')

        if not email:
            return jsonify({'error': 'Invalid input'}), 400

        if email not in users:
            return jsonify({'error': 'User not found'}), 404

        # Per esempio, si può simulare l'invio dell'email di reset
        return jsonify({'message': 'Password reset email sent'}), 200

    return render_template('reset_password.html')

# Pagina principale simile a Netflix
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000, debug=True)
