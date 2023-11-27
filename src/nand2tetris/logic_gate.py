# define the not gate
def not_(x: bool) -> bool:
    return nand(x, x)


# define the and gate
def and_(x: bool, y: bool) -> bool:
    return not_(nand(x, y))


# define the or gate
def or_(x: bool, y: bool) -> bool:
    return nand(nand(x, x), nand(y, y))


# define the nor gate
def nor(x: bool, y: bool) -> bool:
    return not_(or_(x, y))


# define the xor gate
def xor(x: bool, y: bool) -> bool:
    return nand(nand(x, nand(x, y)), nand(nand(x, y), y))


# define the mux gate
def mux(x: bool, y: bool, sel: bool) -> bool:
    return or_(and_(x, not_(sel)), and_(y, sel))


# define the dmux gate
def dmux(x: bool, sel: bool) -> bool:
    return and_(x, not_(sel)), and_(x, sel)


def nand(x: bool, y: bool) -> bool:
    if not isinstance(x, bool) or not isinstance(y, bool):
        raise TypeError("Inputs must be of type bool.")

    if x and y:
        return False
    elif x and not y:
        return True
    elif not x and y:
        return True
    elif not x and not y:
        return True
    else:
        ValueError("Unexpected combination of input values.")
