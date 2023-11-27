from nand2tetris.logic_gate import not_, and_, or_, xor
from typing import List


def half_adder(x: bool, y: bool) -> bool:
    return xor(x, y), and_(x, y)


# define the full adder
def full_adder(x: bool, y: bool, c: bool) -> bool:
    # return _xor(_xor(x, y), c), _or(_and(x, y), _and(_xor(x, y), c))
    return half_adder(half_adder(x, y)[0], c)[0], or_(
        half_adder(x, y)[1], half_adder(half_adder(x, y)[0], c)[1]
    )


# define the adder
def adder(x: bool, y: bool) -> bool:
    if len(x) != len(y):
        raise ValueError("The two input lists must be of the same length.")

    if len(x) == 1:
        return [full_adder(x[0], y[0], False)[0]]
    else:
        return full_adder(x[0], y[0], False)[0] + adder(x[1:], y[1:])


# define the incrementer
def incrementer(x: bool) -> bool:
    return adder(x, [False] + [True] * (len(x) - 1))


# define the ALU
def alu(
    x: List[bool],
    y: List[bool],
    zx: bool,
    nx: bool,
    zy: bool,
    ny: bool,
    f: bool,
    no: bool,
) -> List[bool]:
    if zx:
        x = [False] * len(x)
    if nx:
        x = not_(x)
    if zy:
        y = [False] * len(y)
    if ny:
        y = not_(y)
    if f:
        out = adder(x, y)
    else:
        out = and_(x, y)
    if no:
        out = not_(out)
    return out, or_(and_(not_(x), not_(y)), and_(x, y))
