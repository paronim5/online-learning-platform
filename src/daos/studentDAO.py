from daos.DAOInterface import DaoInterface
from database.databaseSingleton import DatabaseConnection as conn
from models.student import Student
from utils.logger import log

class StudentDAO(DaoInterface):
    def __init__(self):
        super().__init__()
        self._db_con = conn()
        conn().select_database("online_learning_platform")

    def register_with_course(self, student: Student, course_id: int, initial_score: float = 0) -> bool:
        """
        Transactional Insert: Creates a student and enrolls them in a course.
        """
        query_student = "INSERT INTO students (name, email, registration_date) VALUES (%s, %s, %s)"
        query_enrollment = "INSERT INTO enrollments (student_id, course_id, final_score) VALUES (%s, %s, %s)"
        
        try:
            cursor = self._db_con.connection.cursor()
            
            # 1. Insert Student
            log(f"Transactional Insert Step 1: Creating student {student.name}")
            cursor.execute(query_student, (student.name, student.email, student.registration_date))
            student_id = cursor.lastrowid
            
            # 2. Insert Enrollment
            log(f"Transactional Insert Step 2: Enrolling student {student_id} in course {course_id}")
            cursor.execute(query_enrollment, (student_id, course_id, initial_score))
            
            self._db_con.connection.commit()
            log("Transaction Committed Successfully.")
            return True
        except Exception as e:
            self._db_con.connection.rollback()
            log(f"Transaction Failed (Rolled Back): {e}", "ERROR")
            return False
        finally:
            if 'cursor' in locals(): cursor.close()

    def delete_with_enrollments(self, student_id) -> bool:
        """
        Transactional Delete: Deletes a student and all their enrollments.
        """
        delete_enrollments = "DELETE FROM enrollments WHERE student_id = %s"
        delete_student = "DELETE FROM students WHERE id = %s"
        
        try:
            cursor = self._db_con.connection.cursor()
            
            log(f"Transactional Delete Step 1: Removing enrollments for student {student_id}")
            cursor.execute(delete_enrollments, (student_id,))
            
            log(f"Transactional Delete Step 2: Removing student {student_id}")
            cursor.execute(delete_student, (student_id,))
            
            self._db_con.connection.commit()
            log("Transaction Committed Successfully.")
            return True
        except Exception as e:
            self._db_con.connection.rollback()
            log(f"Transaction Failed (Rolled Back): {e}", "ERROR")
            return False
        finally:
            if 'cursor' in locals(): cursor.close()

    def get_all(self) -> list:
        query = "SELECT id, name, email, registration_date FROM students"
        students =[]
        try:
            #easier mapping 
            cursor = self._db_con.connection.cursor(dictionary=True)
            log(f"executing command {query}")

            cursor.execute(query)
            log(f"Success: {query[:30]}...")

            rows = cursor.fetchall()

            for row in rows:
                student = Student(id=row['id'],
                                  name=row['name'],
                                  email=row['email'],
                                  registration_date=row['registration_date']
                                  )
                students.append(student)
            log(f"Successfully fetched {len(students)} students.")
        except Exception as e:
            log(f"Command failed: {e}", "ERROR")

        finally:
            if 'cursor' in locals():
                cursor.close()
            return students
    
    def get_by_id(self, id) -> Student:
        query = "SELECT id, name, email, registration_date FROM students WHERE id = %s"
        student = None
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            log(f"Executing command: {query} with ID: {id}")
            # comma must be there becase we must provide tuple (or list) without it we can't execute this statement
            cursor.execute(query, (id,))
            log(f"Success: {query[:30]}...")

            row = cursor.fetchone()

            if row:
                student = Student(
                    id=row['id'],
                    name=row['name'],
                    email=row['email'],
                    registration_date=row['registration_date']
                )
                log(f"Successfully fetched student: {student.name}")
            else:
                log(f"No student found with ID: {id}", "WARNING")

        except Exception as e:
            log(f"Command failed: {e}", "ERROR")

        finally:
            if 'cursor' in locals():
                cursor.close()
            return student
    
    def save(self, student: Student) -> int:
        query = "INSERT INTO students (name, email, registration_date) VALUES (%s, %s, %s)"
        params = (student.name, student.email, student.registration_date)
        inserted_id = None
        try:
            cursor = self._db_con.connection.cursor()
            log(f"Executing command: {query}")
            
            cursor.execute(query, params)
            self._db_con.connection.commit() # Save changes
            
            inserted_id = cursor.lastrowid
            log(f"Success: Record inserted with ID {inserted_id}")
        except Exception as e:
            log(f"Command failed: {e}", "ERROR")
            self._db_con.connection.rollback() # Undo on error
        finally:
            if 'cursor' in locals():
                cursor.close()
            return inserted_id

    def update(self, id, student: Student) -> bool:
        query = "UPDATE students SET name = %s, email = %s, registration_date = %s WHERE id = %s"
        # The id goes at the end to match the WHERE clause placeholder
        params = (student.name, student.email, student.registration_date, id)
        success = False
        try:
            cursor = self._db_con.connection.cursor()
            log(f"Executing command: {query}")
            
            cursor.execute(query, params)
            self._db_con.connection.commit()
            
            if cursor.rowcount > 0:
                success = True
                log(f"Success: Student with ID {id} updated.")
            else:
                log(f"No student found with ID {id} to update.", "WARNING")
                
        except Exception as e:
            log(f"Command failed: {e}", "ERROR")
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
            log(f"Executing command: {query} with ID: {id}")
            
            cursor.execute(query, (id,))
            self._db_con.connection.commit()
            
            if cursor.rowcount > 0:
                success = True
                log(f"Success: Student with ID {id} deleted.")
            else:
                log(f"No student found with ID {id} to delete.", "WARNING")
                
        except Exception as e:
            log(f"Command failed: {e}", "ERROR")
            self._db_con.connection.rollback()
        finally:
            if 'cursor' in locals():
                cursor.close()
            return success