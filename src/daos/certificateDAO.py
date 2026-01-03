from daos.DAOInterface import DaoInterface
from database.databaseSingleton import DatabaseConnection as conn
from models.certificate import Certificate

class CertificateDAO(DaoInterface):
    def __init__(self):
        super().__init__()
        self._db_con = conn()

    def get_all(self):
        query = "SELECT * FROM certificates"
        certs = []
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor.fetchall(): certs.append(Certificate(**row))
        finally:
            if 'cursor' in locals(): cursor.close()
            return certs

    def get_by_id(self, id):
        query = "SELECT * FROM certificates WHERE id = %s"
        cert = None
        try:
            cursor = self._db_con.connection.cursor(dictionary=True)
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            if row: cert = Certificate(**row)
        finally:
            if 'cursor' in locals(): cursor.close()
            return cert

    def save(self, cert: Certificate):
        query = "INSERT INTO certificates (student_id, course_id, issue_date, certificate_number, is_verified) VALUES (%s,%s,%s,%s,%s)"
        params = (cert.student_id, cert.course_id, cert.issue_date, cert.certificate_number, cert.is_verified)
        return self._commit(query, params)

    def update(self, id, cert: Certificate):
        query = "UPDATE certificates SET student_id=%s, course_id=%s, issue_date=%s, certificate_number=%s, is_verified=%s WHERE id=%s"
        params = (cert.student_id, cert.course_id, cert.issue_date, cert.certificate_number, cert.is_verified, id)
        return self._commit(query, params)

    def delete(self, id):
        return self._commit("DELETE FROM certificates WHERE id = %s", (id,))

    def _commit(self, query, params):
        try:
            cursor = self._db_con.connection.cursor()
            cursor.execute(query, params)
            self._db_con.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error: {e}"); self._db_con.connection.rollback(); return False
        finally:
            if 'cursor' in locals(): cursor.close()