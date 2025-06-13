def reverse_words(text):
    words = text.split(" ")
    new_text = ""

    for word in words:
        reversed_word = ""
        for letter in word:
            reversed_word = letter + reversed_word
        new_text = new_text + reversed_word + " "

    return new_text[:-1]