from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('productos', __name__, url_prefix='/productos')

@bp.route('/', methods=['GET'])
def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Producto")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@bp.route('/', methods=['POST'])
def crear():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Producto (nombre, descripcion, stock, precio) VALUES (%s, %s, %s, %s)",
                   (data['nombre'], data['descripcion'], data['stock'], data['precio']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Producto creado'}), 201