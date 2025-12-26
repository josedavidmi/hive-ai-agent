import os
from pyhive import hive
from dotenv import load_dotenv

load_dotenv()

def get_hive_connection():
    return hive.Connection(
        host=os.getenv("HIVE_HOST"),
        port=int(os.getenv("HIVE_PORT")),
        username=os.getenv("HIVE_USER"),
        database=os.getenv("HIVE_DATABASE")
    )

def run_query(sql):
    with get_hive_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall(), [desc[0] for desc in cursor.description]