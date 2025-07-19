def descending_order(num):
    digits = list(str(num))

    for i in range(len(digits)):
        for j in range(0, len(digits) - i - 1):
            if digits[j] < digits[j + 1]:
                temp = digits[j]
                digits[j] = digits[j + 1]
                digits[j + 1] = temp

    result = ""
    for digit in digits:
        result += digit

    return int(result)