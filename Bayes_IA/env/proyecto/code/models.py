from config import db

class Prediccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    edad = db.Column(db.Integer)
    genero = db.Column(db.Integer)
    ocupacion = db.Column(db.Integer)
    nivel_educativo = db.Column(db.Integer)
    estado_civil = db.Column(db.Integer)
    salario = db.Column(db.Integer)
    puntaje_credito = db.Column(db.Integer)
    prediccion = db.Column(db.Integer)
