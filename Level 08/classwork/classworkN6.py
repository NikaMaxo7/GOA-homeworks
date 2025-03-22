# BONUS ) მომხმარბელს შემოყავს N-ინტეჯერი, 
# იპოვეთ N-ის ფესვი, თუ ვერ იპოვეთ გამოიტანეთ false

n = int(input("enter number: "))

if n < 0:
    print(False)
else:
    found = False
    for i in range(n + 1):
        if i * i == n:
            print(i)
            found = True
            break
    if not found:
        print(False)
