from daos.DAOInterface import DaoInterface
from database.databaseSingleton import DatabaseConnection as conn
from models.enrollment import Enrollment
from utils.logger import log

class EnrollmentDAO(DaoInterface):
    def __init__(self):
        super().__init__()
        self._db_con = conn()

    def get_all(self) -> list:
        query = "SELECT * FROM enrollments"
        results = []
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor.fetchall(): results.append(Enrollment(**row))
        except Exception as e: log(f"Error: {e}", "ERROR")
        finally:
            if 'cursor' in locals(): cursor.close()
            return results

    def get_by_id(self, ids: tuple) -> Enrollment:
        # ids = (student_id, course_id)
        query = "SELECT * FROM enrollments WHERE student_id = %s AND course_id = %s"
        res = None
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            cursor.execute(query, ids)
            row = cursor.fetchone()
            if row: res = Enrollment(**row)
        finally:
            if 'cursor' in locals(): cursor.close()
            return res

    def save(self, enrollment: Enrollment) -> bool:
        query = "INSERT INTO enrollments (student_id, course_id, progress_percentage, final_score, is_completed) VALUES (%s, %s, %s, %s, %s)"
        params = (enrollment.student_id, enrollment.course_id, enrollment.progress_percentage, enrollment.final_score, enrollment.is_completed)
        return self._run_query(query, params)

    def update(self, ids: tuple, enrollment: Enrollment) -> bool:
        query = "UPDATE enrollments SET progress_percentage=%s, final_score=%s, is_completed=%s WHERE student_id=%s AND course_id=%s"
        params = (enrollment.progress_percentage, enrollment.final_score, enrollment.is_completed, ids[0], ids[1])
        return self._run_query(query, params)

    def delete(self, ids: tuple) -> bool:
        return self._run_query("DELETE FROM enrollments WHERE student_id=%s AND course_id=%s", ids)

    def _run_query(self, query, params) -> bool:
        try:
            cursor = self._db_con.connection.cursor()
            cursor.execute(query, params)
            self._db_con.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            log(f"Error: {e}", "ERROR"); self._db_con.connection.rollback(); return False
        finally:
            if 'cursor' in locals(): cursor.close()
