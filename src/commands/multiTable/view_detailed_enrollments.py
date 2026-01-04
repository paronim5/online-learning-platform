from commands.base.command import Command
from daos.enrollmentDAO import EnrollmentDAO

class ViewDetailedEnrollmentsCommand(Command):
    def __init__(self, dao: EnrollmentDAO):
        self.dao = dao

    def execute(self) -> bool:
        print("\n--- Detailed Enrollments (Multi-Table Join) ---")
        results = self.dao.get_all_detailed()
        if not results:
            print("No enrollments found.")
            return True
            
        print(f"{'Student':<20} | {'Email':<25} | {'Course':<20} | {'Progress':<10} | {'Score':<5}")
        print("-" * 90)
        for row in results:
            print(f"{row['student_name']:<20} | {row['email']:<25} | {row['course_title']:<20} | {row['progress_percentage']:<10} | {row['final_score']}")
        return True

    def undo(self):
        pass
