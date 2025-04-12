from flask import Flask, request, jsonify

app = Flask(__name__)

# Crear arreglos para cada sensor
sensor_data = {f'sensor{i}': [] for i in range(1, 17)}

@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    try:
        datos = request.get_json()
        for i in range(1, 17):
            sensor_key = f'sensor{i}'
            if sensor_key in datos:
                sensor_data[sensor_key].append(datos[sensor_key])
        return jsonify({"message": "Datos guardados correctamente", "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": "Error al guardar datos", "error": str(e)}), 400

@app.route('/obtener_datos', methods=['GET'])
def obtener_datos():
    return jsonify(sensor_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
