from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('info_contacto', __name__, url_prefix='/api/contactos')

@bp.route('/', methods=['GET'])
def listar():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM InformacionContacto")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@bp.route('/', methods=['POST'])
def crear():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO InformacionContacto (id_usuario, direccion, telefono, email) VALUES (%s, %s, %s, %s)",
                   (data['id_usuario'], data['direccion'], data['telefono'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({'mensaje': 'Contacto guardado'}), 201