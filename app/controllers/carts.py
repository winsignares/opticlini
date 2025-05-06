from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('carritos', __name__, url_prefix='/carritos')

@bp.route('/', methods=['GET'])
def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Carrito")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@bp.route('/', methods=['POST'])
def crear():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Carrito (id_usuario, total) VALUES (%s, %s)",
                   (data['id_usuario'], data['total']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Carrito creado'}), 201