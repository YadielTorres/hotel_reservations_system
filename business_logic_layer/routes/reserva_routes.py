# routes/reserva_routes.py
@reserva_bp.route('/', methods=['POST'])
@login_required
def create_reserva():

"""
Crear una nueva reserva para el cliente autenticado.
Parámetros:
- habitacion_id: ID de la habitación a reservar.
- fecha_inicio: Fecha de inicio de la reserva.
- fecha_fin: Fecha de fin de la reserva.
Retorna:
- JSON con mensaje de éxito o error.
"""


    data = request.get_json()
    habitacion_id = data['habitacion_id']
    fecha_inicio = data['fecha_inicio']
    fecha_fin = data['fecha_fin']
    cliente_id = current_user.id
    
    cursor = db.connection.cursor()
    cursor.execute("""
        INSERT INTO reservas (cliente_id, habitacion_id, fecha_inicio, fecha_fin)
        VALUES (%s, %s, %s, %s)
    """, (cliente_id, habitacion_id, fecha_inicio, fecha_fin))
    
    db.connection.commit()
    return jsonify({'message': 'Reserva creada exitosamente'}), 201
