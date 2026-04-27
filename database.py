import mysql.connector
from config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    INFRAESTRUCTURACOMUN_DB_NAME,
    APROVISIONAMIENTO_DB_NAME,
    PEDIDOS_DB_NAME,
)

# Función privada para conectar (Igual que tu otro proyecto)
def _connect(database: str):
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=database,
    )

# --- Funciones de conexión ---

def get_aprovisionamiento_connection():
    return _connect(APROVISIONAMIENTO_DB_NAME)

def get_pedidos_connection():
    return _connect(PEDIDOS_DB_NAME)

def get_infraestructuracomun_connection():
    return _connect(INFRAESTRUCTURACOMUN_DB_NAME)

# --- Mejora para tu práctica: El Ejecutor Universal ---

def run_query(connection_func, sql: str):
    """
    Esta función te permite ejecutar SQL en cualquier base de datos
    sin tener que abrir y cerrar el cursor a mano cada vez.
    """
    conn = connection_func()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    finally:
        # Esto asegura que la conexión se cierre aunque haya un error
        cursor.close()
        conn.close()