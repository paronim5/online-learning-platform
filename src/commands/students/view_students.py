from commands.base.command import Command
from daos.studentDAO import StudentDAO

class ViewStudentsCommand(Command):
    def __init__(self, dao: StudentDAO): self.dao = dao
    def execute(self) -> bool:
        items = self.dao.get_all()
        print("\n--- Students ---")
        for i in items: print(f"{i.id} | {i.name} | {i.email}")
        return False
    def undo(self): pass
