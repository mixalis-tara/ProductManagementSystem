import psycopg2

class DatabaseConnection:

    def execute_query(self, query: str, params: tuple):
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()
            cursor.execute(query, params)
            return conn, cursor
        except Exception as e:
            print(f"An unexpected error occurred while executing query: {e}")
            return None, None



    def fetch_data(self, query: str):
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result