from typing import Optional
from commands.base.command import Command
from daos.studentDAO import StudentDAO
from models.student import Student
from utils.input_helper import get_int_input

class UpdateStudentCommand(Command):
    def __init__(self, dao: StudentDAO):
        self.dao = dao
        self.target_id: Optional[int] = None
        self.old_state: Optional[Student] = None

    def execute(self) -> bool:
        self.target_id = get_int_input("Student ID to update: ")
        if not self.target_id: return False
        
        curr = self.dao.get_by_id(self.target_id)
        if not curr:
            print("[-] Student not found.")
            return False
        
        self.old_state = curr
        print(f"Current: {curr}")
        
        name = input(f"New Name ({curr.name}): ").strip() or curr.name
        email = input(f"New Email ({curr.email}): ").strip() or curr.email
        
        try:
            new_s = Student(name, email, curr.registration_date, id=self.target_id)
            if self.dao.update(self.target_id, new_s):
                print("[+] Updated.")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.target_id and self.old_state:
            self.dao.update(self.target_id, self.old_state)
