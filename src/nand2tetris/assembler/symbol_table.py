class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_entry(self, symbol, address):
        self.table[symbol] = address

    def contains(self, symbol) -> bool:
        return symbol in self.table

    def get_address(self, symbol) -> str:
        return self.table[symbol]
