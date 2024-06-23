from config import app, db
from predictor import hacer_prediccion_blueprint

# Registrar el blueprint para la predicción
app.register_blueprint(hacer_prediccion_blueprint)

# Endpoint de prueba para la conexión a la base de datos
@app.route('/test_db')
def test_db():
    try:
        # Realiza una consulta simple para verificar la conexión
        result = db.session.execute('SELECT 1').scalar()
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
