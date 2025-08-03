def scramble(strng, array):
    result = [""] * len(strng)

    i = 0
    while i < len(strng):
        position = array[i]
        result[position] = strng[i]
        i = i + 1

    final_string = ""
    j = 0
    while j < len(result):
        final_string = final_string + result[j]
        j = j + 1

    return final_string