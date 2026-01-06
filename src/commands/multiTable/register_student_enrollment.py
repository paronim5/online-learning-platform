from commands.base.command import Command
from daos.studentDAO import StudentDAO
from daos.courseDAO import CourseDAO
from models.student import Student
from utils.input_helper import get_int_input
from utils.logger import log
import datetime

class RegisterStudentToCourseCommand(Command):
    def __init__(self, student_dao: StudentDAO, course_dao: CourseDAO):
        self.student_dao = student_dao
        self.course_dao = course_dao

    def execute(self) -> bool:
        print("\n--- Register Student & Enroll (Transactional) ---")
        name = input("Student Name: ")
        email = input("Student Email: ")
        
        course_id = None
        choice = input("Identify Course by (1) ID or (2) Name? [1]: ").strip()
        
        if choice == '2':
            search_term = input("Enter Course Name (partial): ").strip()
            found_courses = self.course_dao.search_by_title(search_term)
            
            if not found_courses:
                log("No courses found matching that name.", "WARNING")
                return False
            
            if len(found_courses) == 1:
                c = found_courses[0]
                print(f"Found: {c.title} (ID: {c.id}, Level: {c.level})")
                confirm = input("Is this correct? (Y/N): ").strip().upper()
                if confirm == 'Y':
                    course_id = c.id
                else:
                    return False
            else:
                print(f"Found {len(found_courses)} courses:")
                for c in found_courses:
                    print(f" - ID: {c.id} | {c.title} | {c.level}")
                course_id = get_int_input("Enter the ID of the course to select: ")
        else:
            course_id = get_int_input("Course ID to Enroll: ")
        
        if not name or not email or not course_id:
            log("Invalid input provided.", "WARNING")
            return False

        reg_date = datetime.date.today()
        student = Student(name, email, reg_date)
        
        if self.student_dao.register_with_course(student, course_id):
            log("Successfully registered student and enrolled in course.")
            return True
        return False

    def undo(self):
        log("Undo not implemented for complex transaction yet.", "WARNING")
