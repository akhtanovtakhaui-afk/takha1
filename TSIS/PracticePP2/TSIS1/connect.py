import psycopg2#создаёт соединение с базой данных
from config import load_config

def connect():
    config = load_config()
    return psycopg2.connect(**config)