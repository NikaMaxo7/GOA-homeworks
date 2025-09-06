def most_frequent_char(s):
    max_count = 0
    result = ""

    for i in s:
        count = 0
        for j in s:
            if i == j:
                count = count + 1

        if count > max_count:
            max_count = count
            result = i

    return result