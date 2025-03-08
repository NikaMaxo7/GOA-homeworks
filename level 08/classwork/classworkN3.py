# 3) მომხმარებეს შემოატანინეთ სამ ასოიანი სიტყვა, 
# თუ  მან არ შემოიყვანა სამი ასო მაშინ გამოუპრინტეთ 
# რომ მან უნდა შეიყვანოს ზუსტად სამი ასო და გაუშვას პროგრამა თავიდან. 
# როდესაც მომხმარებელი შეიყვანს სამ ასოიან სიტყვას, 
# შეამოწმეთ არის თუ არა ის პალინდრომი 
# და გაოუტანეთ True ან False შესაბამისად

while True:
    word = input("enter word: ")

    if len(word) == 3:
        if word[0] == word[2]:
            print(True)
        else:
            print(False)
        break
    else:
        print("Please enter exactly three letters!")
