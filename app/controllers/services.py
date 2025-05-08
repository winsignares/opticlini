from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('servicios', __name__, url_prefix='/api/servicios')

@bp.route('/', methods=['GET'])
def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Servicio")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@bp.route('/', methods=['POST'])
def crear():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Servicio (nombre, descripcion, precio) VALUES (%s, %s, %s)",
                   (data['nombre'], data['descripcion'], data['precio']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Servicio creado'}), 201