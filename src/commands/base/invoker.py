from typing import List
from commands.base.command import Command

class CommandInvoker:
    def __init__(self):
        self._history: List[Command] = []

    def execute_command(self, command: Command):
        if command.execute():
            self._history.append(command)

    def undo_last_command(self):
        if not self._history:
            print("\n[!] No commands to undo.")
            return

        command = self._history.pop()
        print(f"\n[Undo] Reverting {command.__class__.__name__}...")
        command.undo()
