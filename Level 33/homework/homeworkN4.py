def get_count(sentence):
    vowel1 = "a"
    vowel2 = "e"
    vowel3 = "i"
    vowel4 = "o"
    vowel5 = "u"
    vowels_in_string = 0
    for i in sentence:
        if vowel1 in i:
            vowels_in_string += 1
        elif vowel2 in i:
            vowels_in_string += 1
        elif vowel3 in i:
            vowels_in_string += 1
        elif vowel4 in i:
            vowels_in_string += 1
        elif vowel5 in i:
            vowels_in_string += 1
    return vowels_in_string