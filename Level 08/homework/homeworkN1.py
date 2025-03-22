num = int(input("enter number: "))

while num > 50:
    num = int(input("enter number again: "))

if num <= 50:
    for i in range(1,101):
        answer = num * i
        if answer > 100:
            break
        print(f"{num}*{i}=" + str(answer))
