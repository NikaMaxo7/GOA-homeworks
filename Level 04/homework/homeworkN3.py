score = int(input("შეიყვანეთ პროექტში მიღებული ქულა: "))

if score > 90:
    print("Grade: A")
elif score > 75:
    print("Grade: B")
elif score > 60:
    print("Grade: C")
elif score > 50:
    print("Grade: D")
elif score > 40:
    print("Grade: E")
elif score > 30:
    print("Grade: F")
else:
    print("You didn't get enough points.")
