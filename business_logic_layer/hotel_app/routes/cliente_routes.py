# routes/cliente_routes.py
from flask import Blueprint, jsonify, request
from models import db
from flask_login import login_required

cliente_bp = Blueprint('clientes', __name__)
@cliente_bp.route('/', methods=['GET'])
@login_required
def get_clientes():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    clientes = []
    for row in rows:
        cliente = {
            'id': row[0],
            'nombre': row[1],
            'direccion':row[2],
            'telefono':row[3],
            'email':row[4],
            'fecha_registro': row[5].strftime('%Y-%m-%d%H:%M:%S')
        }
        clientes.append(cliente)
    return jsonify(clientes)
    
@cliente_bp.route('/<int:id>', methods=['GET'])
@login_required
def get_cliente(id):
    #Obtener un cliente por ID
    pass
    
@cliente_bp.route('/', methods=['POST'])
@login_required
def create_cliente():
    data = request.get_json()
    nombre = data['nombre']
    direccion = data.get('direccion', '')
    telefono = data.get('telefono', '')
    email = data['email']
    
    cursor = db.connection.cursor()
    cursor.execute("""
        INSERT INTO clientes (nombre, direccion, telefono, email)
        VALUES (%s, %s, %s, %s)
    """, (nombre, direccion, telefono, email))
    db.connection.commit()
    return jsonify({'message': 'Cliente creado exitosamente'}),201
    
    try:
        cursor.execute("""
            INSERT INTO clientes (nombre, direccion, telefono, email)
            VALUES (%s, %s, %s, %s)
        """, (nombre, direccion, telefono, email))
        db.connection.commit()
    except IntegrityError:
        return jsonify({'message': 'El email ya está registrado'}), 400

    
@cliente_bp.route('/<int:id>', methods=['PUT'])
@login_required
def update_cliente(id):
    # Actualizar un cliente existente
    pass
@cliente_bp.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_cliente(id):
    #Eliminar un cliente
    pass
