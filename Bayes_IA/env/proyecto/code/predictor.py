from flask import Blueprint, request, jsonify
import joblib
from models import db, Prediccion

hacer_prediccion_blueprint = Blueprint('hacer_prediccion', __name__)

# Cargar el modelo entrenado
modelo = joblib.load('modelo_entrenado2.pkl')

@hacer_prediccion_blueprint.route('/api/prediccion', methods=['POST'])
def hacer_prediccion():
    data = request.json
    # Realizar la predicción usando los datos recibidos
    try:
        # Extraer características del JSON recibido
        caracteristicas = [
            int(data['edad']),
            int(data['genero']),
            int(data['ocupacion']),
            int(data['nivel_educativo']),
            int(data['estado_civil']),
            int(data['salario']),
            int(data['puntaje_credito'])
        ]
    
        # Hacer la predicción
        prediccion = modelo.predict([caracteristicas])[0]
        
        # Guardar la predicción y los datos en la base de datos
        nueva_prediccion = Prediccion(
            edad=int(data['edad']),
            genero=int(data['genero']),
            ocupacion=int(data['ocupacion']),
            nivel_educativo=int(data['nivel_educativo']),
            estado_civil=int(data['estado_civil']),
            salario=int(data['salario']),
            puntaje_credito=int(data['puntaje_credito']),
            prediccion=int(prediccion)  # Convertir la predicción a int
        )
        db.session.add(nueva_prediccion)
        db.session.commit()
        
        # Devolver la respuesta JSON con la predicción
        return jsonify({'prediccion': int(prediccion)})  # Convertir la predicción a int
    except Exception as e:
        # Manejar cualquier error y devolver una respuesta con el error
        return jsonify({'error': str(e)}), 500
