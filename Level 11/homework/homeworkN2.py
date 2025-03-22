def string_clean(s):
    a = ""
    for i in s:
        if i not in "1234567890":
            a += i
    return a
