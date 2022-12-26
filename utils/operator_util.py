import operator

OPERATORS = {
    '*': lambda x, y: operator.mul(int(x), int(y)),
    '+': lambda x, y: operator.add(int(x), int(y)),
    '^': lambda x, y: operator.pow(int(x), int(y))
}

def get_operation(operator, value1, value2):
    return OPERATORS[operator]