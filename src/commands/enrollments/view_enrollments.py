from commands.base.command import Command
from daos.enrollmentDAO import EnrollmentDAO

class ViewEnrollmentsCommand(Command):
    def __init__(self, dao: EnrollmentDAO): self.dao = dao
    def execute(self) -> bool:
        items = self.dao.get_all()
        print("\n--- Enrollments ---")
        for i in items: print(f"Student: {i.student_id} | Course: {i.course_id} | Progress: {i.progress_percentage}%")
        return False
    def undo(self): pass
