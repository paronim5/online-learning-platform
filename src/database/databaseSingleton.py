from mysql.connector import Error
import mysql.connector as mysql
import os 
# without it .env file in not loading properly 
from dotenv import load_dotenv
load_dotenv()

class DatabaseConnection:
    _instance = None 
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                cls._connection = mysql.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASS"),
                )
                print("--- Database Connection Established ---")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                cls._connection = None
        return cls._instance

    @property
    def connection(self):
        return self._connection