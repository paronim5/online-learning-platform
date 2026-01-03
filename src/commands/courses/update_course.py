from typing import Optional
from commands.base.command import Command
from daos.courseDAO import CourseDAO
from models.course import Course
from utils.input_helper import get_int_input, get_float_input

class UpdateCourseCommand(Command):
    def __init__(self, dao: CourseDAO):
        self.dao = dao
        self.target_id: Optional[int] = None
        self.old_state: Optional[Course] = None

    def execute(self) -> bool:
        self.target_id = get_int_input("Course ID to update: ")
        if not self.target_id: return False
        
        curr = self.dao.get_by_id(self.target_id)
        if not curr: return False
        self.old_state = curr
        
        title = input(f"Title ({curr.title}): ").strip() or curr.title
        price = get_float_input(f"Price ({curr.price}): ") 
        if price is None: price = curr.price
        
        try:
            # For simplicity, only updating title and price in this menu, keeping others
            new_obj = Course(title, curr.instructor_id, curr.duration_hours, curr.level, price, id=self.target_id)
            if self.dao.update(self.target_id, new_obj):
                print("[+] Updated.")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.target_id and self.old_state:
            self.dao.update(self.target_id, self.old_state)
