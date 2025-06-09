def accum(st):
    result = []

    for i in range(len(st)):
        letter = st[i]
        big_letter = letter.upper()
        small_letters = letter.lower() * i
        word = big_letter + small_letters
        result.append(word)

    final_result = "-".join(result)
    return final_result