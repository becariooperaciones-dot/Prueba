import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "3306") # El "3306" es un salvavidas por si falla el .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

INFRAESTRUCTURACOMUN_DB_NAME = os.getenv("INFRAESTRUCTURACOMUN_DB_NAME")
APROVISIONAMIENTO_DB_NAME = os.getenv("APROVISIONAMIENTO_DB_NAME")
PEDIDOS_DB_NAME = os.getenv("PEDIDOS_DB_NAME")