from daos.DAOInterface import DaoInterface
from database.databaseSingleton import DatabaseConnection as conn
from models.student import Student
class StudentDAO(DaoInterface):
    def __init__(self):
        super().__init__()
        self._db_con = conn()
        conn().select_database("online_learning_platform")

    def get_all(self) -> list:
        query = "SELECT id, name, email, registration_date FROM students"
        students =[]
        try:
            #easier mapping 
            cursor = self._db_con.connection.cursor(dictionary=True)
            print(f"executing command {query}")

            cursor.execute(query)
            print(f"Success: {query[:30]}...")

            rows = cursor.fetchall()

            for row in rows:
                student = Student(id=row['id'],
                                  name=row['name'],
                                  email=row['email'],
                                  registration_date=row['registration_date']
                                  )
                students.append(student)
            print(f"Successfully fetched {len(students)} students.")
        except Exception as e:
            print(f"Command failed: {e}")

        finally:
        # 4. Always close your cursor!
            if 'cursor' in locals():
                cursor.close()
            return students
    
    def get_by_id(self, id) -> Student:
        query = "SELECT id, name, email, registration_date FROM students WHERE id = %s"
        raise NotImplementedError
    
    def save(self, object) -> bool:
        query = "INSERT INTO students (name, email, registration_date) VALUES (%s, %s, %s)"
        raise NotImplementedError
    
    def update(self, id) -> bool:
        query = "UPDATE students SET name = %s, email = %s, registration_date = %s WHERE id = %s"
        raise NotImplementedError
    
    def delete(self, id) -> bool:
        query = "DELETE FROM students WHERE id = %s"
        raise NotImplementedError