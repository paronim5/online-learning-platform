from typing import Optional
from commands.base.command import Command
from daos.certificateDAO import CertificateDAO
from models.certificate import Certificate
from utils.input_helper import get_int_input

class UpdateCertificateCommand(Command):
    def __init__(self, dao: CertificateDAO):
        self.dao = dao
        self.target_id: Optional[int] = None
        self.old_state: Optional[Certificate] = None

    def execute(self) -> bool:
        self.target_id = get_int_input("Certificate ID to update: ")
        if not self.target_id: return False
        
        curr = self.dao.get_by_id(self.target_id)
        if not curr: return False
        self.old_state = curr
        
        cert_num = input(f"Certificate Number ({curr.certificate_number}): ").strip() or curr.certificate_number
        
        try:
            # We only allow updating cert number for simplicity here
            new_obj = Certificate(curr.student_id, curr.course_id, cert_num, curr.issue_date, curr.is_verified, id=self.target_id)
            if self.dao.update(self.target_id, new_obj):
                print("[+] Updated.")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.target_id and self.old_state:
            self.dao.update(self.target_id, self.old_state)
