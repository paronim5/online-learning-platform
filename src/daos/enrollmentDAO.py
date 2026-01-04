from daos.DAOInterface import DaoInterface
from database.databaseSingleton import DatabaseConnection as conn
from models.enrollment import Enrollment
from utils.logger import log

class EnrollmentDAO(DaoInterface):
    def __init__(self):
        super().__init__()
        self._db_con = conn()

    def get_all_detailed(self) -> list:
        """
        Fetches detailed enrollment information including student name and course title.
        """
        query = """
        SELECT 
            e.student_id, s.name as student_name, s.email,
            e.course_id, c.title as course_title, 
            e.progress_percentage, e.final_score
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
        """
        results = []
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            log(f"Executing complex query: {query}")
            cursor.execute(query)
            results = cursor.fetchall()
            log(f"Fetched {len(results)} detailed enrollments.")
        except Exception as e:
            log(f"Error fetching detailed enrollments: {e}", "ERROR")
        finally:
            if 'cursor' in locals(): cursor.close()
            return results

    def update_score_and_student_email(self, student_id, course_id, new_score, new_email) -> bool:
        """
        Transactional Update: Updates student email and enrollment score.
        """
        update_student = "UPDATE students SET email = %s WHERE id = %s"
        update_enrollment = "UPDATE enrollments SET final_score = %s WHERE student_id = %s AND course_id = %s"
        
        try:
            cursor = self._db_con.connection.cursor()
            
            log(f"Transactional Update Step 1: Updating email for student {student_id}")
            cursor.execute(update_student, (new_email, student_id))
            
            log(f"Transactional Update Step 2: Updating score for course {course_id}")
            cursor.execute(update_enrollment, (new_score, student_id, course_id))
            
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
