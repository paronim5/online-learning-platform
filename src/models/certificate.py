
from datetime import date
 
class Certificate:
    def __init__(self, student_id, course_id, certificate_number, 
                 issue_date=None, is_verified=True, id=None):
        self._id = id
        self._student_id = student_id
        self._course_id = course_id
        self.certificate_number = certificate_number
        self.issue_date = issue_date or date.today()
        self.is_verified = is_verified

    @property
    def id(self): return self._id

    @property
    def student_id(self): return self._student_id

    @property
    def course_id(self): return self._course_id


    @property
    def certificate_number(self): return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        if not value or len(value) > 50:
            raise ValueError("Certificate number is required and must be < 50 chars.")
        self._certificate_number = value

    def __str__(self):
        return f"Certificate {self._certificate_number} for Student {self._student_id}"

    def __eq__(self, other):
        if not isinstance(other, Certificate): return False
        return self.certificate_number == other.certificate_number