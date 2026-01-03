from typing import Optional
from commands.base.command import Command
from daos.instructorDAO import InstructorDAO
from models.instructor import Instructor

class CreateInstructorCommand(Command):
    def __init__(self, dao: InstructorDAO):
        self.dao = dao
        self.created_id: Optional[int] = None

    def execute(self) -> bool:
        print("\n--- Create Instructor ---")
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        bio = input("Bio: ").strip()
        
        if not name or not email: return False
        try:
            inst = Instructor(name, email, bio)
            self.created_id = self.dao.save(inst)
            if self.created_id:
                print(f"[+] Instructor created (ID: {self.created_id})")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.created_id: self.dao.delete(self.created_id)
