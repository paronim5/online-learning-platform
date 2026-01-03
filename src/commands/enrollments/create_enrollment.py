from typing import Optional, Tuple
from commands.base.command import Command
from daos.enrollmentDAO import EnrollmentDAO
from models.enrollment import Enrollment
from utils.input_helper import get_int_input
from utils.logger import logger

class CreateEnrollmentCommand(Command):
    def __init__(self, dao: EnrollmentDAO):
        self.dao = dao
        self.created_key: Optional[Tuple[int, int]] = None

    def execute(self) -> bool:
        print("\n--- Enroll Student ---")
        sid = get_int_input("Student ID: ")
        cid = get_int_input("Course ID: ")
        
        if not sid or not cid: return False
        try:
            enr = Enrollment(sid, cid)
            if self.dao.save(enr):
                self.created_key = (sid, cid)
                logger.info(f"[+] Enrolled Student {sid} in Course {cid}")
                return True
        except Exception as e: logger.error(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.created_key: self.dao.delete(self.created_key)
