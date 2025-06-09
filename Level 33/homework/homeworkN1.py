def manual_split(text):
    result = []
    word = ""

    for letter in text:
        if letter != " ":
            word = word + letter
        else:
            if word != "":
                result.append(word)
                word = ""

    if word != "":
        result.append(word)

    return result