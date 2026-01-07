import datetime
import os

LOG_FILE = "log.txt"

def log(message: str, level: str = "INFO"):
    """
    Logs a message to the console and to a file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] [{level}] {message}"

    print(formatted_message)

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted_message + "\n")
    except Exception as e:
        print(f"[{timestamp}] [ERROR] Failed to write to log file: {e}")

class SimpleLogger:
    def info(self, message):
        log(message, "INFO")
    
    def error(self, message):
        log(message, "ERROR")
    
    def warning(self, message):
        log(message, "WARNING")

logger = SimpleLogger()
