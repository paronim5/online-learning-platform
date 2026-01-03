from typing import Optional
from commands.base.command import Command
from daos.certificateDAO import CertificateDAO
from models.certificate import Certificate
from utils.input_helper import get_int_input

class DeleteCertificateCommand(Command):
    def __init__(self, dao: CertificateDAO):
        self.dao = dao
        self.target_id: Optional[int] = None
        self.deleted_obj: Optional[Certificate] = None

    def execute(self) -> bool:
        self.target_id = get_int_input("Certificate ID to delete: ")
        if not self.target_id: return False
        self.deleted_obj = self.dao.get_by_id(self.target_id)
        if self.dao.delete(self.target_id):
            print("[+] Deleted.")
            return True
        return False

    def undo(self):
        if self.deleted_obj:
            new_id = self.dao.save(self.deleted_obj)
            print(f"[Undo] Restored Certificate (New ID: {new_id})")
