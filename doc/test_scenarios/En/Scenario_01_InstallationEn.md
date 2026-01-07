# SPSE Jecna Test Case 
 
**Test Case ID:** INST_01  
**Test Designed by:** Pavlo Kosov 
**Test Name:** Application Installation and Setup  
**Brief description:** Verify that the environment is correctly set up, dependencies are installed, and the database is imported.  
**Pre-conditions:** Python 3.10+ and MySQL Server 8.0+ must be installed on the machine.  
**Dependencies and Requirements:** Internet connection (for pip), MySQL Credentials (root/password).  
 
| Step | Test Steps | Test Data | Expected Result | Notes |
|------|------------|-----------|-----------------|-------|
| 1 | Open Command Prompt/PowerShell and check Python version. | `python --version` | Output shows Python 3.10 or higher. | |
| 2 | Check MySQL version. | `mysql --version` | Output confirms MySQL is installed. | |
| 3 | Install dependencies using pip. | `pip install -r requirements.txt` | Packages `mysql-connector-python` and `python-dotenv` install successfully. | |
| 4 | Configure environment variables. | Create `.env` file with `DB_HOST`, `DB_USER`, `DB_PASS`. | File is saved in project src/utils/.env. | |
| 5 | Initialize Database. | Run `bin/init_db.bat` (or `python src/database/databaseSchema.py`) | Script executes and prints "Database Schema & Data Imported Successfully". | |
| 6 | Launch the application. | `bin/run.bat` (or `python src/main.py`) | Application starts and displays the Main Menu. | |
| 7 | Exit the application. | Option `9` | Application closes with "Goodbye!". | |
