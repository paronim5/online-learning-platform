from databaseSingleton import DatabaseConnection
db = DatabaseConnection()

cursor = db.connection.cursor()
query = "SELECT * FROM certificates"

cursor.execute(query)
result = cursor.fetchall()

for _ in result:
    print(_)