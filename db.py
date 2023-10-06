from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)

# Cargar la configuración desde un archivo externo (config.py)
app.config.from_pyfile('config.py')

# Configuración de SQLAlchemy para SQLite o MySQL
if app.config['DB_TYPE'] == 'sqlite':
    # SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
else:
    # MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + app.config['DB_USERNAME'] + ':' + app.config['DB_PASSWORD'] + '@' + app.config['DB_HOST'] + '/' + app.config['DB_NAME']

# Inicializar SQLAlchemy con la configuración de la aplicación
db = SQLAlchemy(app)

# Definir modelos de la base de datos

# Lista de campañas
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    message_variables = db.Column(db.Integer, nullable=False)
    campaign_type = db.Column(db.String(10), nullable=False)

# Campaña SMS
class SMS_Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    dni = db.Column(db.String(20), nullable=False)
    message_variables_data = db.Column(db.Text)
    is_sent = db.Column(db.Boolean)
    
# Campaña Email
class Email_Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    email_address = db.Column(db.String(255), nullable=False)
    dni = db.Column(db.String(20), nullable=False)
    message_variables_data = db.Column(db.Text)
    is_sent = db.Column(db.Boolean)

# Modelo de usuario 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)  # Almacena el hash de la contraseña
    salt = db.Column(db.String(32), nullable=False)  # Almacena el valor del salt



# Crear las tablas en la base de datos (esto se ejecutará al llamar a este archivo)
if __name__ == '__main__':
    db.create_all()
