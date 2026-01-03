from commands.base.command import Command
from daos.certificateDAO import CertificateDAO

class ViewCertificatesCommand(Command):
    def __init__(self, dao: CertificateDAO): self.dao = dao
    def execute(self) -> bool:
        items = self.dao.get_all()
        print("\n--- Certificates ---")
        for i in items: print(f"{i.id} | No: {i.certificate_number} | Student: {i.student_id} | Course: {i.course_id}")
        return False
    def undo(self): pass
