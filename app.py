from flask import Flask, jsonify, request
from flask_cors import CORS
from googleapiclient.discovery import build
from google.oauth2 import service_account

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# API Key de Google y ID de la hoja
# API_KEY = "AIzaSyDpb07gNzQKMk1DOGdHZQ4vIpUwZGU_-jg"
# SPREADSHEET_ID = "1fEpTIZWqHod7Fxu5Zp48rUJWgs302ivXR3Y0M2AES7o"
# RANGE_NAME = "Hoja1!A1:E10"  # Modifica según el rango de tu hoja

# Credenciales para la API de Google Sheets
# SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'  # Ruta a tu archivo de credenciales
# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE
# )

# Arreglos para almacenar usuarios y administradores
usuarios = []
admins = []

# Ruta para obtener todos los usuarios
@app.route('/user', methods=['GET'])
def get_users():
    return jsonify(usuarios), 200

# Ruta para crear un nuevo usuario
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    # Validar si faltan datos
    if not data.get('nombre') or not data.get('edad') or not data.get('sexo') or not data.get('altura') or not data.get('peso'):
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    nuevo_usuario = {
        'id': len(usuarios) + 1,
        'nombre': data['nombre'],
        'edad': data['edad'],
        'sexo': data['sexo'],
        'altura': data['altura'],
        'peso': data['peso']
    }
    
    usuarios.append(nuevo_usuario)

    # Simular console.log en Python
    print(f'Usuario creado: {nuevo_usuario}')

    return jsonify({'message': 'Usuario creado exitosamente'}), 201

# Ruta para obtener un usuario por ID
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    usuario = next((user for user in usuarios if user['id'] == user_id), None)
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify(usuario), 200

# Ruta para obtener todos los administradores
@app.route('/admin', methods=['GET'])
def get_admins():
    return jsonify(admins), 200

# Ruta para crear un nuevo administrador
@app.route('/admin', methods=['POST'])
def create_admin():
    data = request.get_json()

    # Validar si faltan datos
    if not data.get('nombre') or not data.get('contrasena') or not data.get('codigo_admin'):
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    nuevo_admin = {
        'id': len(admins) + 1,
        'nombre': data['nombre'],
        'contrasena': data['contrasena'],
        'codigo_admin': data['codigo_admin']
    }

    admins.append(nuevo_admin)

    # Simular console.log en Python
    print(f'Admin creado: {nuevo_admin}')

    return jsonify({'message': 'Admin creado exitosamente'}), 201

# # Ruta para obtener datos de Google Sheets
# @app.route('/spreadsheet', methods=['GET'])
# def get_spreadsheet_data():
#     # Construir el servicio de la API de Google Sheets
#     service = build('sheets', 'v4', credentials=credentials)

#     # Llamar a la API para obtener los datos
#     sheet = service.spreadsheets()
#     result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
#     values = result.get('values', [])

#     if not values:
#         return jsonify({'error': 'No se encontraron datos en la hoja'}), 404

#     # Convertir los datos a una lista de diccionarios
#     headers = values[0]  # Asumimos que la primera fila contiene los encabezados
#     data = [dict(zip(headers, row)) for row in values[1:]]  # Emparejar encabezados con filas

#     return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)
