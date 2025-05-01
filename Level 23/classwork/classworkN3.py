def is_opposite(s1, s2):
    if s1 == "" or s2 == "":
        return False

    return s1.swapcase() == s2