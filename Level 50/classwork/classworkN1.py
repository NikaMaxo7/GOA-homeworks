def square_digits(num):
    answer = ""
    for i in str(num):
        answer += str(int(i) * int(i))
    return int(answer)