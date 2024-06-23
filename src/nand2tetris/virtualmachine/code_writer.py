class VirtualMachineCodeWriter:
    def __init__(self, output_file):
        self.output_file = output_file
        self.label_counter = 0

    def set_file_name(self, file_name):
        self.file_name = file_name

    def write_arithmetic(self, command):
        if command == "add":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("M=D+M\n")
        elif command == "sub":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("M=M-D\n")
        elif command == "neg":
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-M\n")
        elif command == "eq":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("D=M-D\n")
            self.output_file.write("@EQ_TRUE{}\n".format(self.label_counter))
            self.output_file.write("D;JEQ\n")
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=0\n")
            self.output_file.write("@EQ_END{}\n".format(self.label_counter))
            self.output_file.write("0;JMP\n")
            self.output_file.write("(EQ_TRUE{})\n".format(self.label_counter))
            self.output_file.write("@SP\n")
            self.output_file.write("A=M-1\n")
            self.output_file.write("M=-1\n")
            self.output_file.write("(EQ_END{})\n".format(self.label_counter))
            self.label_counter += 1
        elif command == "gt":
            self.output_file.write("@SP\n")
            self.output_file.write("AM=M-1\n")
            self.output_file.write("D=M\n")
            self.output_file.write("A=A-1\n")
            self.output_file.write("D=M-D\n")
            self.output_file.write("@GT_TRUE{}\n".format(self.label_counter))
            self

    def write_push_pop(self, command, segment, index):
        if command == "C_PUSH":
            if segment == "constant":
                self.output_file.write("@{}\n".format(index))
                self.output_file.write("D=A\n")
                self.output_file.write("@SP\n")
                self.output_file.write("A=M\n")
                self.output_file.write("M=D\n")
                self.output_file.write("@SP\n")
                self.output_file.write("M=M+1\n")
        elif command == "C_POP":
            if segment == "constant":
                self.output_file.write("@SP\n")
                self.output_file.write("AM=M-1\n")
                self.output_file.write("D=M\n")
                self.output_file.write("@{}\n".format(index))
                self.output_file.write("M=D\n")
        else:
            raise ValueError("Invalid command type")

    def close(self):
        self.output_file.close()
