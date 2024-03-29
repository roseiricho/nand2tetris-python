class Parser:
    def __init__(self, input_file):
        with open(input_file, "r") as self.file:
            self.commands = self.file.readlines()
            self.executed_line = 0

    def has_more_command(self) -> bool:
        if self.executed_line < len(self.commands):
            return True
        else:
            return False

    # main.pyで呼び出す時にhas_more_commandがTrueのときにだけよびだされるつもりのmethod
    def advance(self):
        while True:
            current_command = self.commands[self.executed_line].strip()
            self.executed_line += 1

            if current_command != "" and current_command[0:2] != "//":
                if "//" in current_command:
                    self.current_command = current_command[
                        : current_command.find("//")
                    ].strip()
                else:
                    self.current_command = current_command
                break

            else:
                pass

    def command_type(self) -> str:
        if "@" in self.current_command:
            return "A_COMMAND"
        elif "(" in self.current_command and ")" in self.current_command:
            return "L_COMMAND"
        elif "=" in self.current_command or ";" in self.current_command:
            return "C_COMMAND"
        else:
            return None

    # main.pyで呼び出す時にA_COMMANDかL_COMMANDときにだけよびだされるつもりのmethod
    def symbol(self) -> str:
        if self.current_command[0] == "@":
            return self.current_command[1:]
        elif self.current_command[0] == "(":
            return self.current_command[1:-1]

    # main.pyで呼び出す時にC_COMMANDときにだけよびだされるつもりのmethod
    def dest(self) -> str:
        if "=" in self.current_command:
            return self.current_command[: self.current_command.find("=")]
        else:
            return "null"

    # main.pyで呼び出す時にC_COMMANDときにだけよびだされるつもりのmethod
    def comp(self) -> str:
        sc = ";" in self.current_command
        eq = "=" in self.current_command
        if eq and sc:
            return self.current_command[
                self.current_command.find("=") + 1 : self.current_command.find(";")
            ]
        elif eq:
            return self.current_command[self.current_command.find("=") + 1 :]
        elif sc:
            return self.current_command[: self.current_command.find(";")]
        else:
            raise ValueError("invalid input.")

    # main.pyで呼び出す時にC_COMMANDときにだけよびだされるつもりのmethod
    def jump(self) -> str:
        if ";" in self.current_command:
            return self.current_command[self.current_command.find(";") + 1 :]
        else:
            return "null"
