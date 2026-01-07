# SPSE Ječná – Testovací případ

**ID testovacího případu:** INST_01  
**Autor testu:** Pavlo Kosov  
**Název testu:** Instalace a nastavení aplikace  
**Stručný popis:** Ověření, že je prostředí správně nastaveno, jsou nainstalovány závislosti a databáze byla úspěšně importována.  
**Prerekvizity:** Na stroji musí být nainstalován Python 3.10+ a MySQL Server 8.0+.  
**Závislosti a požadavky:** Připojení k internetu (pro pip), přihlašovací údaje k MySQL (root/heslo).

| Krok | Testovací kroky                                              | Testovací data                                      | Očekávaný výsledek                                            | Poznámky |
|------|--------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------|----------|
| 1    | Otevřete Příkazový řádek / PowerShell a zkontrolujte verzi Pythonu | `python --version`                                  | Výstup zobrazí Python 3.10 nebo vyšší                        |          |
| 2    | Zkontrolujte verzi MySQL                                     | `mysql --version`                                   | Výstup potvrdí, že je MySQL nainstalováno                     |          |
| 3    | Nainstalujte závislosti pomocí pip                           | `pip install -r requirements.txt`                   | Balíčky mysql-connector-python a python-dotenv se úspěšně nainstalují |          |
| 4    | Nakonfigurujte proměnné prostředí                            | Vytvořte soubor `.env` s DB_HOST, DB_USER, DB_PASS  | Soubor je uložen v `src/utils/.env`                           |          |
| 5    | Inicializujte databázi                                       | `bin/init_db.bat` nebo `python src/database/databaseSchema.py` | Skript se provede a vypíše "Database Schema & Data Imported Successfully" |          |
| 6    | Spusťte aplikaci                                             | `bin/run.bat` nebo `python src/main.py`             | Aplikace se spustí a zobrazí Hlavní menu (Main Menu)          |          |
| 7    | Ukončete aplikaci                                            | Volba 9                                             | Aplikace se zavře s hlášením "Goodbye!"                       |          |