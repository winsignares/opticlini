from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('metodos_pago', __name__, url_prefix='/api/metodos-pago')

@bp.route('/', methods=['GET'])
def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM MetodoPago")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@bp.route('/', methods=['POST'])
def crear():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO MetodoPago (tipo, detalles) VALUES (%s, %s)",
                   (data['tipo'], data['detalles']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Método de pago creado'}), 201