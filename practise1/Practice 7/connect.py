import psycopg2
from config import load_config

def get_connection():
    config = load_config()
    return psycopg2.connect(**config)

if __name__ == '__main__':
    try:
        conn = get_connection()
        print("Connected to the PostgreSQL server.")
        conn.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)