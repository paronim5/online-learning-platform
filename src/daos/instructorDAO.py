from daos.DAOInterface import DaoInterface
from database.databaseSingleton import DatabaseConnection as conn
from models.instructor import Instructor

class InstructorDAO(DaoInterface):
    def __init__(self):
        super().__init__()
        self._db_con = conn()
        conn().select_database("online_learning_platform")

    def get_all(self) -> list:
        query = "SELECT id, name, email, bio, rating, is_verified FROM instructors"
        instructors = []
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor.fetchall():
                instructors.append(Instructor(**row))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if 'cursor' in locals(): cursor.close()
            return instructors

    def get_by_id(self, id) -> Instructor:
        query = "SELECT * FROM instructors WHERE id = %s"
        instructor = None
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row: instructor = Instructor(**row)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if 'cursor' in locals(): cursor.close()
            return instructor

    def save(self, instructor: Instructor) -> bool:
        query = "INSERT INTO instructors (name, email, bio, rating, is_verified) VALUES (%s, %s, %s, %s, %s)"
        params = (instructor.name, instructor.email, instructor.bio, instructor.rating, instructor.is_verified)
        return self._execute_write(query, params)

    def update(self, id, instructor: Instructor) -> bool:
        query = "UPDATE instructors SET name=%s, email=%s, bio=%s, rating=%s, is_verified=%s WHERE id=%s"
        params = (instructor.name, instructor.email, instructor.bio, instructor.rating, instructor.is_verified, id)
        return self._execute_write(query, params)

    def delete(self, id) -> bool:
        query = "DELETE FROM instructors WHERE id = %s"
        return self._execute_write(query, (id,))

    def _execute_write(self, query, params) -> bool:
        success = False
        try:
            cursor = self._db_con.connection.cursor()
            cursor.execute(query, params)
            self._db_con.connection.commit()
            success = cursor.rowcount > 0
        except Exception as e:
            print(f"Error: {e}")
            self._db_con.connection.rollback()
        finally:
            if 'cursor' in locals(): cursor.close()
            return success