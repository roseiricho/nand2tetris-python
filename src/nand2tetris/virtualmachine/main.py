from parser import VirtualMachineParser
from code_writer import VirtualMachineCodeWriter


def main():
    input_file = "./SimpleAdd/SimpleAdd.vm"
    output_file = "./SimpleAdd/SimpleAdd.asm"

    open_input_file = open(input_file, "r")
    open_output_file = open(output_file, "w")

    commands = open_input_file.readlines()
    parser = VirtualMachineParser(commands)
    code_writer = VirtualMachineCodeWriter(open_output_file)

    while parser.has_more_commands():
        result = parser.advance()
        if not result:
            break

        command_type = parser.command_type()
        if command_type == "C_ARITHMETIC":
            code_writer.write_arithmetic(parser.current_command)
        elif command_type == "C_PUSH":
            code_writer.write_push_pop(
                command_type,
                parser.arg1(),
                parser.arg2(),
            )
        elif command_type == "C_POP":
            code_writer.write_push_pop(
                command_type,
                parser.arg1(),
                parser.arg2(),
            )
        else:
            raise ValueError("Invalid command type")

    code_writer.close()


main()
