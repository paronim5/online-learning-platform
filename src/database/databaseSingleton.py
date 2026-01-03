from mysql.connector import Error
import mysql.connector as mysql
import os 
from utils.logger import log
# without it .env file is not loading properly 
from dotenv import load_dotenv
load_dotenv()

class DatabaseConnection:
    _instance = None 
    _connection = None

    def __new__(cls, database_name=None):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                cls._connection = mysql.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASS"),
                )
                log("--- Database Connection Established ---")
            except Error as e:
                log(f"Error connecting to MySQL: {e}", "ERROR")
                cls._connection = None
        return cls._instance
    
    def select_database(self, db_name):
        if self._connection:
            try:
                self._connection.database = db_name
                log(f"--- Switched to database: {db_name} ---")
            except Error as e:
                log(f"Error switching database: {e}", "ERROR")

    @property
    def connection(self):
        return self._connection
    
    @property
    def cursor(self):
        return self._connection