from typing import Optional
from commands.base.command import Command
from daos.studentDAO import StudentDAO
from models.student import Student

class CreateStudentCommand(Command):
    def __init__(self, dao: StudentDAO):
        self.dao = dao
        self.created_id: Optional[int] = None

    def execute(self) -> bool:
        print("\n--- Create Student ---")
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        if not name or not email: return False
        try:
            s = Student(name, email)
            self.created_id = self.dao.save(s)
            if self.created_id:
                print(f"[+] Student created (ID: {self.created_id})")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.created_id: self.dao.delete(self.created_id)
