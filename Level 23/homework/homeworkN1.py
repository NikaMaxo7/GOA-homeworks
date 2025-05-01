def data_type(arg1, arg2):
    if type(arg1) == bool:
        a = int(arg1)
    elif type(arg1) == str:
        if "." in arg1:
            arg1 = float(arg1)
        else:
            arg1 = int(arg1)

    if type(arg2) == bool:
        arg2 = int(arg2)
    elif type(arg2) == str:
        if "." in arg2:
            arg2 = float(arg2)
        else:
            arg2 = int(arg2)

    return arg1 + arg2