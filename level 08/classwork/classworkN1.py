# 1) მომხმარებელს შემოატანინეთ სიტყვა ან წინადადება 
# შეინახეთ ის შეტრიალებულად reversed_string  ცვლადში და 
# გამოიტანეთ ეს ცვლადი

# word = input("enter word: ")
# index = len(word) - 1

# while index >= 0:
#     print(word[index], end="")
#     index -= 1

text = input("input text please: ")
res = ''
for i in text:
    res = i + res
print(res)
