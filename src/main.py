from database.databaseSingleton import DatabaseConnection as conn
from database.databaseSchema import DatabaseSchema
from daos.studentDAO import StudentDAO

# DatabaseSchema()


studentslist = StudentDAO().get_all()

for _ in studentslist:
    print(_)