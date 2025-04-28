```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from itsdangerous import URLSafeTimedSerializer
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['SECURITY_PASSWORD_SALT'] = 'your_password_salt'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
serializer = URLSafeTimedSerializer(app.config['JWT_SECRET_KEY'])

logging.basicConfig(filename='auth.log', level=logging.INFO)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    mfa_secret = db.Column(db.String(120), nullable=True)

def encrypt_data(data):
    return bcrypt.generate_password_hash(data).decode('utf-8')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = encrypt_data(data['password'])
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'username': user.username})
        logging.info(f"Successful login for user: {user.username}")
        return jsonify(access_token=access_token), 200
    logging.warning(f"Failed login attempt for user: {data['username']}")
    return jsonify(message="Invalid credentials"), 401

@app.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user:
        token = serializer.dumps(user.username, salt=app.config['SECURITY_PASSWORD_SALT'])
        # Send token via email (omitted for brevity)
        return jsonify(message="Password reset link sent"), 200
    return jsonify(message="User not found"), 404

@app.route('/reset-password/<token>', methods=['POST'])
def confirm_reset_password(token):
    try:
        username = serializer.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=3600)
        user = User.query.filter_by(username=username).first()
        if user:
            data = request.get_json()
            user.password = encrypt_data(data['new_password'])
            db.session.commit()
            return jsonify(message="Password reset successful"), 200
    except Exception:
        return jsonify(message="Invalid or expired token"), 400

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```