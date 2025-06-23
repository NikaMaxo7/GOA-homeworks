def accum(st):
    result = ""
    for i in range(len(st)):
        result += st[i].upper() + (st[i].lower() * i)
        if i < len(st) - 1:
            result += "-"
    return result