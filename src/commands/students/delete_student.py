from typing import Optional
from commands.base.command import Command
from daos.studentDAO import StudentDAO
from models.student import Student
from utils.input_helper import get_int_input

class DeleteStudentCommand(Command):
    def __init__(self, dao: StudentDAO):
        self.dao = dao
        self.target_id: Optional[int] = None
        self.deleted_obj: Optional[Student] = None

    def execute(self) -> bool:
        self.target_id = get_int_input("Student ID to delete: ")
        if not self.target_id: return False
        
        self.deleted_obj = self.dao.get_by_id(self.target_id)
        if not self.deleted_obj:
            print("[-] Not found.")
            return False
            
        if self.dao.delete(self.target_id):
            print("[+] Deleted.")
            return True
        return False

    def undo(self):
        if self.deleted_obj:
            new_id = self.dao.save(self.deleted_obj)
            print(f"[Undo] Restored Student (New ID: {new_id})")
