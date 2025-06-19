def check_vowel(strng, position):
    vowels = "aeiou"

    if position < 0 or position >= len(strng):
        return False

    letter = strng[position]

    letter = letter.lower()

    if letter in vowels:
        return True
    else:
        return False