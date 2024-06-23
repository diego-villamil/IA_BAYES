from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:TSY!VHzGrN(]FxGt@localhost/proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión SQLAlchemy
db = SQLAlchemy(app)
CORS(app)
