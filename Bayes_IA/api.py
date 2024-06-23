from flask import Flask, jsonify, request
from sklearn.externals import joblib
import mysql.connector

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('modelo_entrenado.pkl')

# Conectar a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="proyecto"
)

# Ruta para recibir datos del formulario y realizar la predicción
@app.route('/api/prediccion', methods=['POST'])
def obtener_datos_formulario():
    datos_formulario = request.json  # Obtener los datos del formulario enviado desde React

    # Realizar la predicción utilizando el modelo
    resultado_prediccion = model.predict([[datos_formulario['edad'],
                                           datos_formulario['genero'],
                                           datos_formulario['ocupacion'],
                                           datos_formulario['nivel_educativo'],
                                           datos_formulario['estado_civil'],
                                           datos_formulario['salario'],
                                           datos_formulario['puntaje_credito']]])

    # Guardar los datos del formulario y el resultado de la predicción en la base de datos
    cursor = mydb.cursor()
    sql = """INSERT INTO prediccion (edad, genero, ocupacion, nivel_educativo, estado_civil, salario, puntaje_credito, prediccion)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (datos_formulario['edad'], datos_formulario['genero'], datos_formulario['ocupacion'],
              datos_formulario['nivel_educativo'], datos_formulario['estado_civil'], datos_formulario['salario'],
              datos_formulario['puntaje_credito'], int(resultado_prediccion[0]))
    cursor.execute(sql, values)
    mydb.commit()
    cursor.close()

    # Devolver el resultado de la predicción
    return jsonify({'prediccion': int(resultado_prediccion[0])})

if __name__ == '__main__':
    app.run(debug=True)
