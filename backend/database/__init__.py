import psycopg2
from config import config

def tuples_to_dict(results, columns):
    parsed_results = [dict(zip(columns, row)) for row in results]
    return parsed_results


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_params):
        self.connection = psycopg2.connect(**db_params)

    def execute_query(self, query: str, columns: list = None):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        if columns is not None:
            result = tuples_to_dict(result, columns)
        cursor.close()
        return result

    def insert(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)


db_params = {
    'host': config.get("POSTGRES_HOST"),
    'port': config.get("POSTGRES_PORT", 5252),
    'database': config.get("POSTGRES_DB"),
    'user': config.get("POSTGRES_USER"),
    'password': config.get("POSTGRES_PASSWORD")
}

db = Database(db_params)
