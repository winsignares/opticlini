from flask import Blueprint, request, jsonify
from app.db import get_connection

bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@bp.route('/', methods=['GET'])
def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Usuario")
    usuarios = cursor.fetchall()
    conn.close()
    return jsonify(usuarios)

@bp.route('/', methods=['POST'])
def crear_usuario():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Usuario (nombre, email, contraseña, telefono)
        VALUES (%s, %s, %s, %s)
    """, (data['nombre'], data['email'], data['contraseña'], data['telefono']))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Usuario creado"}), 201

@bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Usuario SET nombre=%s, email=%s, contraseña=%s, telefono=%s
        WHERE id_usuario=%s
    """, (data['nombre'], data['email'], data['contraseña'], data['telefono'], id))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Usuario actualizado"})

@bp.route('/<int:id>', methods=['GET'])
def obtener_usuario(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Usuario WHERE id_usuario = %s", (id,))
    usuario = cursor.fetchone()
    conn.close()
    return jsonify(usuario or {})

@bp.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuario WHERE id_usuario = %s", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Usuario eliminado"})