from typing import Optional
from commands.base.command import Command
from daos.instructorDAO import InstructorDAO
from models.instructor import Instructor
from utils.input_helper import get_int_input

class UpdateInstructorCommand(Command):
    def __init__(self, dao: InstructorDAO):
        self.dao = dao
        self.target_id: Optional[int] = None
        self.old_state: Optional[Instructor] = None

    def execute(self) -> bool:
        self.target_id = get_int_input("Instructor ID to update: ")
        if not self.target_id: return False
        
        curr = self.dao.get_by_id(self.target_id)
        if not curr: return False
        self.old_state = curr
        
        name = input(f"Name ({curr.name}): ").strip() or curr.name
        email = input(f"Email ({curr.email}): ").strip() or curr.email
        bio = input(f"Bio ({curr.bio}): ").strip() or curr.bio
        
        try:
            new_obj = Instructor(name, email, bio, curr.rating, curr.is_verified, id=self.target_id)
            if self.dao.update(self.target_id, new_obj):
                print("[+] Updated.")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.target_id and self.old_state:
            self.dao.update(self.target_id, self.old_state)
