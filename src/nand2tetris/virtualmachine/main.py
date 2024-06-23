from nand2tetris.virtualmachine.parser import Parser
from nand2tetris.virtualmachine.code_writer import CodeWriter


def main():
    parser = Parser("./SimpleAdd/SimpleAdd.vm")
    code_writer = CodeWriter("./SimpleAdd/SimpleAdd.asm")

    while parser.has_more_command():
        parser.advance()
        if parser.command_type() == "C_ARITHMETIC":
            code_writer.write_arithmetic(parser.current_command)
        elif parser.command_type() == "C_PUSH":
            code_writer.write_push_pop("push", parser.arg1(), parser.arg2())
        elif parser.command_type() == "C_POP":
            code_writer.write_push_pop("pop", parser.arg1(), parser.arg2())
        else:
            raise ValueError("Invalid command type")

    code_writer.close()


main()
