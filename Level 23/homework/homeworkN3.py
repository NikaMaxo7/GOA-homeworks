def string_sum(arg1, arg2):
    result = ""

    if type(arg1) == str and type(arg2) == str:
        result = arg1 + " " + arg2

    elif type(arg1) == str and type(arg2) == int:
        result = arg1 + " " + str(arg2)

    elif type(arg1) == int and type(arg2) == str:
        result = arg2 + " " + str(arg1)

    elif type(arg1) == int and type(arg2) == int:
        result = str(arg1) + str(arg2)

    return result