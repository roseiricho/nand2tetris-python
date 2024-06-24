from typing import List, AnyStr


class VirtualMachineParser:
    def __init__(self, commands: List[AnyStr]):
        self.commands = commands
        self.current_command = None

    def has_more_commands(self):
        return self.current_command is not None or self._has_more_lines()

    def advance(self) -> bool:
        if self.current_command is None:
            return False
        self.current_command = self._next_line()
        return True

    def command_type(self):
        if self.current_command.startswith("push"):
            return "C_PUSH"
        elif self.current_command.startswith("pop"):
            return "C_POP"
        elif self.current_command.startswith("label"):
            return "C_LABEL"
        elif self.current_command.startswith("goto"):
            return "C_GOTO"
        elif self.current_command.startswith("if-goto"):
            return "C_IF"
        elif self.current_command.startswith("function"):
            return "C_FUNCTION"
        elif self.current_command.startswith("return"):
            return "C_RETURN"
        elif self.current_command.startswith("call"):
            return "C_CALL"
        else:
            return "C_ARITHMETIC"

    def arg1(self):
        if self.command_type() == "C_ARITHMETIC":
            return self.current_command
        else:
            return self.current_command.split()[1]

    def arg2(self):
        return int(self.current_command.split()[2])

    def _has_more_lines(self):
        return self.commands

    def _next_line(self):
        if not self.commands:
            return None
        return self.commands.pop(0)
