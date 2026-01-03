from typing import Optional
from commands.base.command import Command
from daos.certificateDAO import CertificateDAO
from models.certificate import Certificate
from utils.input_helper import get_int_input

class CreateCertificateCommand(Command):
    def __init__(self, dao: CertificateDAO):
        self.dao = dao
        self.created_id: Optional[int] = None

    def execute(self) -> bool:
        print("\n--- Issue Certificate ---")
        sid = get_int_input("Student ID: ")
        cid = get_int_input("Course ID: ")
        cert_num = input("Certificate Number: ").strip()
        
        if not sid or not cid or not cert_num: return False
        try:
            cert = Certificate(sid, cid, cert_num)
            self.created_id = self.dao.save(cert)
            if self.created_id:
                print(f"[+] Certificate issued (ID: {self.created_id})")
                return True
        except Exception as e: print(f"[!] Error: {e}")
        return False

    def undo(self):
        if self.created_id: self.dao.delete(self.created_id)
