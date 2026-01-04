from commands.base.command import Command
from daos.studentDAO import StudentDAO
from utils.input_helper import get_int_input
from utils.logger import log

class DeleteStudentCascadeCommand(Command):
    def __init__(self, dao: StudentDAO):
        self.dao = dao

    def execute(self) -> bool:
        print("\n--- Delete Student & Enrollments (Transactional) ---")
        sid = get_int_input("Student ID to delete: ")
        
        if not sid: return False
        
        confirm = input(f"Are you sure you want to delete Student {sid} AND all their enrollments? (y/n): ")
        if confirm.lower() != 'y':
            return False

        if self.dao.delete_with_enrollments(sid):
            log(f"Student {sid} and associated data deleted.")
            return True
        return False

    def undo(self):
        pass
