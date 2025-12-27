from database.databaseSingleton import  DatabaseConnection
from pathlib import Path
class DatabaseSchema:
    def __init__(self):
        self._db_con = DatabaseConnection()
        self._schema_path = Path(__file__).resolve().parent.parent / "sqlCommands" / "schema.sql"
        self._views_path = Path(__file__).resolve().parent.parent / "sqlCommands" / "views.sql"
        self._inserts_path = Path(__file__).resolve().parent.parent / "sqlCommands" / "inserts.sql"
        try:
            self._create_database_schema()
            self._create_views()
            self._insert_data()
        except Exception as e:
            print(e)
        finally:
            self._db_con.connection.close()

    def _create_database_schema(self):
        try:
            with open(self._schema_path, "r", encoding='utf-8') as file:
                sql_script = file.read()

            commands = sql_script.split(';')
            
            cursor = self._db_con.connection.cursor()
            
            print(f"Executing schema from: {self._schema_path}")

            for command in commands:
                # Remove whitespace and check if the command is not empty
                clean_command = command.strip()
                
                if clean_command:
                    try:
                        cursor.execute(clean_command)
                        print(f"Success: {clean_command[:30]}...") 
                    except Exception as cmd_error:
                        print(f"Command failed: {cmd_error}")

            self._db_con.connection.commit()
            print("--- Schema applied successfully ---")
        except Exception as e :
            print(f"error applying schema {e}")
            self._db_con.connection.rollback()


    def _create_views(self):
        try:
            with open(self._views_path, "r", encoding='utf-8') as file:
                sql_script = file.read()

            commands = sql_script.split(';')
            
            cursor = self._db_con.connection.cursor()
            
            print(f"Executing views script from: {self._views_path}")

            for command in commands:
                clean_command = command.strip()
                
                if clean_command:
                    try:
                        cursor.execute(clean_command)
                        print(f"Success: {clean_command[:30]}...") 
                    except Exception as cmd_error:
                        print(f"Command failed: {cmd_error}")

            self._db_con.connection.commit()
            print("--- views are created successfully ---")
        except Exception as e :
            print(f"error creating views{e}")
            self._db_con.connection.rollback()

    def _insert_data(self):
        try:
            with open(self._inserts_path, "r", encoding='utf-8') as file:
                sql_script = file.read()

            commands = sql_script.split(';')
            
            cursor = self._db_con.connection.cursor()
            
            print(f"inserting data from: {self._inserts_path}")

            for command in commands:
                clean_command = command.strip()
                
                if clean_command:
                    try:
                        cursor.execute(clean_command)
                        print(f"Success: {clean_command[:30]}...") 
                    except Exception as cmd_error:
                        print(f"Command failed: {cmd_error}")

            self._db_con.connection.commit()
            print("--- views are created successfully ---")
        except Exception as e :
            print(f"error creating views{e}")
            self._db_con.connection.rollback()



    
    
