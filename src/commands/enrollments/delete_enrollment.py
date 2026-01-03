from typing import Optional, Tuple
from commands.base.command import Command
from daos.enrollmentDAO import EnrollmentDAO
from models.enrollment import Enrollment
from utils.input_helper import get_int_input

class DeleteEnrollmentCommand(Command):
    def __init__(self, dao: EnrollmentDAO):
        self.dao = dao
        self.target_key: Optional[Tuple[int, int]] = None
        self.deleted_obj: Optional[Enrollment] = None

    def execute(self) -> bool:
        print("\n--- Delete Enrollment ---")
        sid = get_int_input("Student ID: ")
        cid = get_int_input("Course ID: ")
        if not sid or not cid: return False
        
        self.target_key = (sid, cid)
        self.deleted_obj = self.dao.get_by_id(self.target_key)
        
        if self.dao.delete(self.target_key):
            print("[+] Deleted.")
            return True
        return False

    def undo(self):
        if self.deleted_obj:
            self.dao.save(self.deleted_obj)
            print("[Undo] Restored Enrollment.")
