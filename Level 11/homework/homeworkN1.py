def calculator(x, y, op):
    if type(x) != int and type(x) != float:
        return "unknown value"
    if type(y) != int and type(y) != float:
        return "unknown value"
    
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            return "unknown value"
        return x / y
    else:
        return "unknown value"
