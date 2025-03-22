# 4)მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა, 
# შემდეგ ამ სიტყვიდან გამოიტანეთ მხოლოდ 'A' ასოები, 
# თუ არ შეიცავს 'A'ს გამოიტანეთ ცარიელი სტრინგი

word = input("enter word: ")
result = ""

for letter in word:
    if letter == 'A':
        result += letter

print(result)
