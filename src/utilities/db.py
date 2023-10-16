import MySQLdb
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class DB:
    def __init__(self):
        try:
            self.connection = MySQLdb.connect(
                host=os.getenv("DATABASE_HOST"),
                user=os.getenv("DATABASE_USERNAME"),
                passwd=os.getenv("DATABASE_PASSWORD"),
                db=os.getenv("DATABASE"),
                autocommit=True,
                ssl_mode="VERIFY_IDENTITY",
                ssl={"ca": os.getenv("DATABASE_SSL_CA")},
                wait_timeout=180
            )
        except MySQLdb.Error as e:
            raise Exception(f"Database connection error: {e}")
    def connection(self):
        try:
            self.connection.ping(reconnect=True)
        except MySQLdb.Error as e:
            raise Exception(f"Database connection error: {e}")

    def __del__(self):
        self.connection.close()

    def insert(self, table, values):
        self.connection()
        try:
            with self.connection.cursor() as cursor:
                columns = ', '.join(values.keys())
                placeholders = ', '.join(['%s'] * len(values))
                query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
                cursor.execute(query, list(values.values()))
                return True
        except (MySQLdb.Error, Exception) as e:
            # Log the error or raise an exception for proper error handling
            print("Error:", e)
            return False
        finally:
            cursor.close()

    # Additional methods for database operations
