def is_palindrome(): 
    word = input("Enter a word: ")
    
    if word == word[::-1]:
        return "The word is a palindrome"
    else:
        return "The word is not a palindrome"

print(is_palindrome())