from database.databaseSingleton import DatabaseConnection as conn
from database.databaseSchema import DatabaseSchema
from daos.studentDAO import StudentDAO
from models.student import Student

# DatabaseSchema()


studentslist = StudentDAO().get_all()

for _ in studentslist:
    print(_)

studentById = StudentDAO().get_by_id(1)
print(studentById)

# newStudent = Student("Neco", "something@gmail.com")
# saveStudent = StudentDAO().save(newStudent)
# print(saveStudent)

updateStudent = StudentDAO().update(6, Student("fromNecoToNeco2", "halohalo@gmail.com"))
print(updateStudent)
studentById = StudentDAO().get_by_id(6)
print(studentById)

deleteStudent = StudentDAO().delete(6)
print(deleteStudent)