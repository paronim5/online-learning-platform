from commands.base.command import Command
from daos.enrollmentDAO import EnrollmentDAO
from utils.input_helper import get_int_input, get_float_input
from utils.logger import log

class UpdateStudentEnrollmentCommand(Command):
    def __init__(self, dao: EnrollmentDAO):
        self.dao = dao

    def execute(self) -> bool:
        print("\n--- Update Student & Enrollment (Transactional) ---")
        sid = get_int_input("Student ID: ")
        cid = get_int_input("Course ID: ")
        
        if not sid or not cid: return False
        
        new_email = input("New Email: ")
        new_score = get_float_input("New Score: ")
        
        if not new_email or new_score is None:
            log("Invalid input.", "WARNING")
            return False

        if self.dao.update_score_and_student_email(sid, cid, new_score, new_email):
            log("Update successful.")
            return True
        return False

    def undo(self):
        pass
