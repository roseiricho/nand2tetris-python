from code import Code
from parser import Parser
from symbol_table import SymbolTable


def main():
    parser = Parser("./Max.asm")
    code = Code()
    symbol_table = SymbolTable()
    binary = []

    # 1st pass
    address = 0
    while parser.has_more_command():
        parser.advance()
        if parser.command_type() == "L_COMMAND":
            symbol_table.add_entry(parser.symbol(), address)
        elif (
            parser.command_type() == "A_COMMAND" or parser.command_type() == "C_COMMAND"
        ):
            address += 1
        else:
            raise ValueError("Invalid command type")

    # 2nd pass
    parser = Parser("./Max.asm")
    symbol_address = 16
    while parser.has_more_command():
        parser.advance()
        if parser.command_type() == "A_COMMAND":
            if parser.symbol().isnumeric():
                binary.append("0" + format(int(parser.symbol()), "015b"))
            elif not symbol_table.contains(parser.symbol()):
                symbol_table.add_entry(parser.symbol(), symbol_address)
                binary.append("0" + format(symbol_table.next_address, "015b"))
                symbol_address += 1
            else:
                binary.append(
                    "0" + format(symbol_table.get_address(parser.symbol()), "015b")
                )
        elif parser.command_type() == "C_COMMAND":
            binary.append(
                "111"
                + code.comp(parser.comp())
                + code.dest(parser.dest())
                + code.jump(parser.jump())
            )

    with open("./Max.hack", "w") as f:
        for line in binary:
            f.write(line + "\n")


main()
