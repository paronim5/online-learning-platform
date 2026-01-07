from commands.base.command import Command
from daos.enrollmentDAO import EnrollmentDAO
from utils.logger import log

class ViewStudentProgressCommand(Command):
    def __init__(self, enrollment_dao: EnrollmentDAO):
        self.enrollment_dao = enrollment_dao

    def execute(self) -> bool:
        print("\n--- VIEW: Student Progress ---")
        try:
            data = self.enrollment_dao.get_student_progress_view()
            if not data:
                print("No data found in view.")
                return True

            print(f"{'Student':<20} | {'Course':<25} | {'Instructor':<20} | {'Progress':<8} | {'Completed':<5}")
            print("-" * 100)
            for row in data:
                completed = "Yes" if row['is_completed'] else "No"
                print(f"{row['student_name']:<20} | {row['course_title']:<25} | {row['instructor_name']:<20} | {row['progress_percentage']:<8} | {completed:<5}")
            print("-" * 100)
            return True
        except Exception as e:
            log(f"Error displaying student progress: {e}", "ERROR")
            return False

    def undo(self):
        print("Undo not supported for views.")
