def to_alternating_case(string):
    result = ''
    for i in string:
        if 'a' <= i <= 'z':
            result += i.upper()
        elif 'A' <= i <= 'Z':
            result += i.lower()
        else:
            result += i
    return result