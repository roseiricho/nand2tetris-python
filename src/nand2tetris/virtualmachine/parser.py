class VirtualMachineParser:
    input_file = None

    def __init__(self, input_file):
        self.input_file = input_file
        self.current_command = None

    def has_more_commands(self):
        return self.current_command is not None or self.input_file.has_more_lines()

    def advance(self):
        self.current_command = self.input_file.next_line()

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
