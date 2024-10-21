from flask import Flask, jsonify, request
from flask_cors import CORS
from decimal import Decimal, InvalidOperation

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

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

    # Convertir la edad a decimal para cálculos, pero almacenar como entero
    try:
        edad_decimal = Decimal(data['edad'])  # Convertir a decimal para operaciones si es necesario
        edad_entero = int(edad_decimal)  # Almacenar solo la parte entera
    except (InvalidOperation, ValueError):
        return jsonify({'error': 'La edad debe ser un número decimal válido'}), 400

    nuevo_usuario = {
        'id': len(usuarios) + 1,
        'nombre': data['nombre'],
        'edad': edad_entero,  # Almacenar como entero
        'sexo': data['sexo'],
        'altura': data['altura'],
        'peso': data['peso']
    }
    
    usuarios.append(nuevo_usuario)

    # Simular console.log en Python
    print(f'Usuario creado: {nuevo_usuario}')

    return jsonify({'message': 'Usuario creado exitosamente', 'usuario': nuevo_usuario}), 201

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

if __name__ == "__main__":
    app.run(debug=True)
