import sys
import os
import subprocess
from pathlib import Path

# Add 'src' directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
if src_dir not in sys.path:
    sys.path.append(src_dir)

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: 'python-dotenv' module not found. Please run 'pip install -r requirements.txt'")
    sys.exit(1)

class DatabaseSchema:
    def __init__(self):
        # Load .env file
        load_dotenv()
        
        self._sql_path = Path(__file__).resolve().parent.parent.parent / "database_export.sql"
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASS", "")

    def apply_schema(self):
        """Imports the SQL file using the mysql command line tool."""
        print(f"--- Starting Database Import from {self._sql_path.name} ---")
        
        if not self._sql_path.exists():
            print(f"Error: File not found: {self._sql_path}")
            return

        # Prepare environment with password for secure passing
        env = os.environ.copy()
        if self.password:
            env["MYSQL_PWD"] = self.password

        # Construct command: mysql -h HOST -u USER
        # The SQL file contains 'CREATE DATABASE' and 'USE', so we don't need to specify DB name here.
        cmd = ["mysql", "-h", self.host, "-u", self.user, "--default-character-set=utf8mb4"]
        
        try:
            print(f"Connecting to MySQL at {self.host} as {self.user}...")
            
            with open(self._sql_path, "r", encoding="utf-8") as f:
                # Run the command piping the file content to stdin
                result = subprocess.run(
                    cmd, 
                    stdin=f, 
                    env=env, 
                    check=True,
                    capture_output=True,
                    text=True
                )
            
            if result.stdout:
                print(result.stdout)
                
            print("\n--- Database Schema & Data Imported Successfully! ---")
            print("--- Tables, Views, and Triggers have been created. ---")
            print("--- You can now run the application. ---")
            
        except subprocess.CalledProcessError as e:
            print("\n--- Import Failed ---")
            print(f"Error Code: {e.returncode}")
            print(f"Error Output:\n{e.stderr}")
            print("Tip: Check your .env credentials and ensure MySQL server is running.")
        except FileNotFoundError:
            print("\n--- Error: 'mysql' command not found. ---")
            print("Please ensure MySQL Client is installed and in your system PATH.")
            print("You can verify this by running 'mysql --version' in your terminal.")
        except Exception as e:
            print(f"\n--- Unexpected Error: {e} ---")

if __name__ == "__main__":
    schema_manager = DatabaseSchema()
    schema_manager.apply_schema()
