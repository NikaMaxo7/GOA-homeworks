# For loop-ის დახმარებით შექმენით პროგრამა, 
# სადაც მომხმარებელი შემოიტანს 
# რიცხვს (50-ის ჩათვლით, თუ არა დაუპრინტეთ, რომ თავიდან შეიყვანოს),
#  და თქვენ გამოიტანეთ ამ რიცხვის ჯერადები 100-ის ჩათვლით.

num = int(input("enter number: "))

while num > 50:
    num = int(input("enter number again: "))

if num <= 50:
    for i in range(1,101):
        answer = num * i
        if answer > 100:
            break
        print(f"{num}*{i}=" + str(answer))