from commands.base.command import Command
from daos.courseDAO import CourseDAO

class ViewCoursesCommand(Command):
    def __init__(self, dao: CourseDAO): self.dao = dao
    def execute(self) -> bool:
        items = self.dao.get_all()
        print("\n--- Courses ---")
        for i in items: print(f"{i.id} | {i.title} | Price: {i.price} | Level: {i.level}")
        return False
    def undo(self): pass
