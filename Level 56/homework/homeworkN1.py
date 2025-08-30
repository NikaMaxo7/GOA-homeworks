def most_frequent_char(s):
    max_count = 0
    result = ""

    for ch in s:
        count = 0
        for other in s:
            if ch == other:
                count = count + 1

        if count > max_count:
            max_count = count
            result = ch

    return result