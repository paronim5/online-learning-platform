from typing import Optional, Tuple
from commands.base.command import Command
from daos.enrollmentDAO import EnrollmentDAO
from models.enrollment import Enrollment
from utils.input_helper import get_int_input, get_float_input

class UpdateEnrollmentCommand(Command):
    def __init__(self, dao: EnrollmentDAO):
        self.dao = dao
        self.target_key: Optional[Tuple[int, int]] = None
        self.old_state: Optional[Enrollment] = None

    def execute(self) -> bool:
        print("\n--- Update Enrollment ---")
        sid = get_int_input("Student ID: ")
        cid = get_int_input("Course ID: ")
        if not sid or not cid: return False
        
        self.target_key = (sid, cid)
        curr = self.dao.get_by_id(self.target_key)
        if not curr:
            print("[-] Enrollment not found.")
            return False
        self.old_state = curr
        
        prog = get_float_input(f"Progress % ({curr.progress_percentage}): ")
        if prog is None: prog = curr.progress_percentage
        
        score = get_float_input(f"Final Score ({curr.final_score}): ")
        if score is None: score = curr.final_score
        
        try:
            new_obj = Enrollment(sid, cid, prog, score, curr.is_completed)
            if self.dao.update(self.target_key, new_obj):
                print("[+] Updated.")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.target_key and self.old_state:
            self.dao.update(self.target_key, self.old_state)
