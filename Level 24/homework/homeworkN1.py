def digitize(n):
    num_as_text = str(n)
    reversed_text = num_as_text[::-1]
    digit_list = []
    for i in reversed_text:
        digit = int(i)
        digit_list.append(digit)
    return digit_list