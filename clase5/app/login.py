from flask import Blueprint, request, jsonify
import mysql.connector 
from mysql.connector import Error

# Configuración de la página de login
login = Blueprint('login', __name__)

DB_CONFIG = {
    "host": "localhost",  # Cambia esto tu usuario de base de datos y el contenedor Docker
    "user": "root",       # Cambia esto al usuario de tu base de datos
    "password": "M4tsum0t017*",  # Cambia esto por tu contraseña de base de datos
    "database": 'jaguarete'         # Nombre del esquema (o 'database') en la base de datos MySQL
}

@login.route('/login', methods=['POST'])
def llamarServicios():
    user = request.json.get('user')
    password = request.json.get('password')
    
    codRes, menRes, usuario, accion = verify_credentials(user, password)
    
    return jsonify({
        "codRes": codRes,
        "menRes": menRes,
        "usuario": usuario,
        "accion": accion
    })

# Aquí iría la función para verificar credenciales:
def verify_credentials(user, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    usuario = None

    try:
        print("Verificar login")
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT username FROM USERS WHERE username = %s AND password = %s"
        cursor.execute(query, (user, password))
        result = cursor.fetchone()

        if result:
            usuario = result['username']
            print("Usuario y contraseña OK")
            accion = "Success"
        else:
            print("Usuario o contraseña incorrecta")
            accion = "Usuario o contraseña incorrecta"
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'

        cursor.close()
        connection.close()

    except Error as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: " + str(e)'
        accion = "Error interno"

    return codRes, menRes, usuario, accion
