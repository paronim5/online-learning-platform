from mysql.connector import Error
import mysql.connector as mysql
import os 

class DatabaseConnection:
    _instance = None 
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                # Initialize the connection once
                cls._connection = mysql.connect(
                    host=os.getenv("db_host"),
                    user=os.getenv("db_user"),
                    password=os.getenv("db_password"),
                    database=os.getenv("db_name"),
                    port=3306
                )
                print("--- Database Connection Established ---")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                cls._connection = None
        return cls._instance

    @property
    def connection(self):
        return self._connection