import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_SERVER = os.getenv('DB_SERVER')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT', 5432)  # PostgreSQL usa 5432 por defecto

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_SERVER,
        database=DB_DATABASE,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return conn