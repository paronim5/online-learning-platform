from commands.base.command import Command
from daos.instructorDAO import InstructorDAO

class ViewInstructorsCommand(Command):
    def __init__(self, dao: InstructorDAO): self.dao = dao
    def execute(self) -> bool:
        items = self.dao.get_all()
        print("\n--- Instructors ---")
        for i in items: print(f"{i.id} | {i.name} | {i.email} | Rating: {i.rating}")
        return False
    def undo(self): pass
