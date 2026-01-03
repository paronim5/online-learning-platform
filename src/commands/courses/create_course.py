from typing import Optional
from commands.base.command import Command
from daos.courseDAO import CourseDAO
from models.course import Course
from utils.input_helper import get_int_input, get_float_input

class CreateCourseCommand(Command):
    def __init__(self, dao: CourseDAO):
        self.dao = dao
        self.created_id: Optional[int] = None

    def execute(self) -> bool:
        print("\n--- Create Course ---")
        title = input("Title: ").strip()
        inst_id = get_int_input("Instructor ID: ")
        duration = get_float_input("Duration (hours): ")
        level = input("Level (Beginner/Intermediate/Advanced/Expert/Master): ").strip()
        price = get_float_input("Price: ") or 0.0

        if not title or not inst_id or not duration or not level:
            print("[!] Missing required fields.")
            return False

        try:
            c = Course(title, inst_id, duration, level, price)
            self.created_id = self.dao.save(c)
            if self.created_id:
                print(f"[+] Course created (ID: {self.created_id})")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.created_id: self.dao.delete(self.created_id)
