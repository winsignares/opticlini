from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('detalle_carrito', __name__, url_prefix='/detalles-carrito')

@bp.route('/', methods=['GET'])
def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM DetalleCarrito")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@bp.route('/', methods=['POST'])
def crear():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO DetalleCarrito (id_carrito, id_producto, cantidad, subtotal) VALUES (%s, %s, %s, %s)",
                   (data['id_carrito'], data['id_producto'], data['cantidad'], data['subtotal']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Detalle de carrito creado'}), 201