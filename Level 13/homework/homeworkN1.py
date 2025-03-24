def res(num):
    x = 0
    for i in str(num):
        x += int(i)
    return num % x

print("answer is " + str(res(int(input("enter: ")))))