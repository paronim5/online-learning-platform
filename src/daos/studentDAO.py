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
            if 'cursor' in locals():
                cursor.close()
            return students
    
    def get_by_id(self, id) -> Student:
        query = "SELECT id, name, email, registration_date FROM students WHERE id = %s"
        student = None
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            print(f"Executing command: {query} with ID: {id}")
            # comma must be there becase we must provide tuple (or list) without it we can't execute this statement
            cursor.execute(query, (id,))
            print(f"Success: {query[:30]}...")

            row = cursor.fetchone()

            if row:
                student = Student(
                    id=row['id'],
                    name=row['name'],
                    email=row['email'],
                    registration_date=row['registration_date']
                )
                print(f"Successfully fetched student: {student.name}")
            else:
                print(f"No student found with ID: {id}")

        except Exception as e:
            print(f"Command failed: {e}")

        finally:
            if 'cursor' in locals():
                cursor.close()
            return student
    
    def save(self, student: Student) -> bool:
        query = "INSERT INTO students (name, email, registration_date) VALUES (%s, %s, %s)"
        params = (student.name, student.email, student.registration_date)
        success = False
        try:
            cursor = self._db_con.connection.cursor()
            print(f"Executing command: {query}")
            
            cursor.execute(query, params)
            self._db_con.connection.commit() # Save changes
            
            print(f"Success: Record inserted with ID {cursor.lastrowid}")
            success = True
        except Exception as e:
            print(f"Command failed: {e}")
            self._db_con.connection.rollback() # Undo on error
        finally:
            if 'cursor' in locals():
                cursor.close()
            return success

    def update(self, id, student: Student) -> bool:
        query = "UPDATE students SET name = %s, email = %s, registration_date = %s WHERE id = %s"
        # The id goes at the end to match the WHERE clause placeholder
        params = (student.name, student.email, student.registration_date, id)
        success = False
        try:
            cursor = self._db_con.connection.cursor()
            print(f"Executing command: {query}")
            
            cursor.execute(query, params)
            self._db_con.connection.commit()
            
            if cursor.rowcount > 0:
                print(f"Success: Student with ID {id} updated.")
                success = True
            else:
                print(f"No student found with ID {id} to update.")
        except Exception as e:
            print(f"Command failed: {e}")
            self._db_con.connection.rollback()
        finally:
            if 'cursor' in locals():
                cursor.close()
            return success

    def delete(self, id) -> bool:
        query = "DELETE FROM students WHERE id = %s"
        success = False
        try:
            cursor = self._db_con.connection.cursor()
            print(f"Executing command: {query} with ID: {id}")
            
            cursor.execute(query, (id,))
            self._db_con.connection.commit()
            
            if cursor.rowcount > 0:
                print(f"Success: Student with ID {id} deleted.")
                success = True
            else:
                print(f"No student found with ID {id} to delete.")
        except Exception as e:
            print(f"Command failed: {e}")
            self._db_con.connection.rollback()
        finally:
            if 'cursor' in locals():
                cursor.close()
            return success