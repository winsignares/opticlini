from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('citas', __name__, url_prefix='/citas')

@bp.route('/', methods=['GET'])
def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Cita")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@bp.route('/', methods=['POST'])
def crear():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cita (fecha, hora, id_usuario, id_servicio, estado) VALUES (%s, %s, %s, %s, %s)",
                   (data['fecha'], data['hora'], data['id_usuario'], data['id_servicio'], data['estado']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Cita creada'}), 201