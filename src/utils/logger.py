import datetime
import os

# Define the log file path relative to the project root (assuming src is one level deep)
# Or just use "log.txt" if the CWD is the project root.
LOG_FILE = "log.txt"

def log(message: str, level: str = "INFO"):
    """
    Logs a message to the console and to a file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] [{level}] {message}"
    
    # Print to console
    print(formatted_message)
    
    # Append to file
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted_message + "\n")
    except Exception as e:
        # Fallback if file writing fails
        print(f"[{timestamp}] [ERROR] Failed to write to log file: {e}")

class SimpleLogger:
    def info(self, message):
        log(message, "INFO")
    
    def error(self, message):
        log(message, "ERROR")
    
    def warning(self, message):
        log(message, "WARNING")

# Create a singleton instance to be used where 'logger' is expected
logger = SimpleLogger()
