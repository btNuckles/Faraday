import operator

def apply_operation(left_operand, right_operand, operator):
    ops = {
        "+": lambda x,y: x+y,
        "-": lambda x,y: x-y,
        "*": lambda x,y: x*y,
        "/": lambda x,y: x/y
    }
    return ops[operator](left_operand, right_operand)
