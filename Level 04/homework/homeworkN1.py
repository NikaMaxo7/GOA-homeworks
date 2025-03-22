age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age > 2 and age < 6:
    print("You should walk in the garden.")
elif age >= 6 and age < 18:
    print("You have to walk to school.")
else:
    print("You have to walk to work.")
