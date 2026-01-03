from daos.DAOInterface import DaoInterface
from database.databaseSingleton import DatabaseConnection as conn
from models.course import Course
from utils.logger import log

class CourseDAO(DaoInterface):
    def __init__(self):
        super().__init__()
        self._db_con = conn()

    def get_all(self) -> list:
        query = "SELECT id, title, instructor_id, price, duration_hours, level FROM courses"
        courses = []
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor.fetchall():
                courses.append(Course(**row))
        except Exception as e:
            log(f"Error: {e}", "ERROR")
        finally:
            if 'cursor' in locals(): cursor.close()
            return courses

    def get_by_id(self, id) -> Course:
        query = "SELECT * FROM courses WHERE id = %s"
        course = None
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row: course = Course(**row)
        finally:
            if 'cursor' in locals(): cursor.close()
            return course

    def save(self, course: Course) -> int:
        query = "INSERT INTO courses (title, instructor_id, price, duration_hours, level) VALUES (%s, %s, %s, %s, %s)"
        params = (course.title, course.instructor_id, course.price, course.duration_hours, course.level)
        return self._execute_insert(query, params)

    def update(self, id, course: Course) -> bool:
        query = "UPDATE courses SET title=%s, instructor_id=%s, price=%s, duration_hours=%s, level=%s WHERE id=%s"
        params = (course.title, course.instructor_id, course.price, course.duration_hours, course.level, id)
        return self._execute_commit(query, params)

    def delete(self, id) -> bool:
        return self._execute_commit("DELETE FROM courses WHERE id = %s", (id,))

    def _execute_commit(self, query, params) -> bool:
        try:
            cursor = self._db_con.connection.cursor()
            cursor.execute(query, params)
            self._db_con.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            log(f"Error: {e}", "ERROR"); self._db_con.connection.rollback(); return False
        finally:
            if 'cursor' in locals(): cursor.close()

    def _execute_insert(self, query, params) -> int:
        try:
            cursor = self._db_con.connection.cursor()
            cursor.execute(query, params)
            self._db_con.connection.commit()
            return cursor.lastrowid
        except Exception as e:
            log(f"Error: {e}", "ERROR"); self._db_con.connection.rollback(); return None
        finally:
            if 'cursor' in locals(): cursor.close()
