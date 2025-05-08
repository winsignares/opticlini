from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('pedidos', __name__, url_prefix='/api/pedidos')

@bp.route('/', methods=['GET'])
def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Pedido")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@bp.route('/', methods=['POST'])
def crear():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Pedido (fecha, id_usuario, id_metodo_pago, total, estado) VALUES (%s, %s, %s, %s, %s)",
                   (data['fecha'], data['id_usuario'], data['id_metodo_pago'], data['total'], data['estado']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Pedido creado'}), 201