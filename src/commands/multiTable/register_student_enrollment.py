from commands.base.command import Command
from daos.studentDAO import StudentDAO
from models.student import Student
from utils.input_helper import get_int_input
from utils.logger import log
import datetime

class RegisterStudentToCourseCommand(Command):
    def __init__(self, dao: StudentDAO):
        self.dao = dao

    def execute(self) -> bool:
        print("\n--- Register Student & Enroll (Transactional) ---")
        name = input("Student Name: ")
        email = input("Student Email: ")
        course_id = get_int_input("Course ID to Enroll: ")
        
        if not name or not email or not course_id:
            log("Invalid input provided.", "WARNING")
            return False

        reg_date = datetime.date.today()
        student = Student(name, email, reg_date)
        
        if self.dao.register_with_course(student, course_id):
            log("Successfully registered student and enrolled in course.")
            return True
        return False

    def undo(self):
        log("Undo not implemented for complex transaction yet.", "WARNING")
