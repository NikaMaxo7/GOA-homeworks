# 1) მომხმარებელს შემოატანინეთ სიტყვა ან წინადადება 
# შეინახეთ ის შეტრიალებულად reversed_string  ცვლადში და 
# გამოიტანეთ ეს ცვლადი

text = input("input text please: ")
res = ''
for i in text:
    res = i + res
print(res)
