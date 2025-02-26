correct_password = "goamagaria"

password = input("enter password: ")

while password != correct_password:
    print("password is incorrect try again")
    password = input("enter password: ") 

print("Congrats, password is correct! ")
