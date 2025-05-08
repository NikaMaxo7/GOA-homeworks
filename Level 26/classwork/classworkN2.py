def multiply(n):
    if n < 0:
        positive_n = -n
    else:
        positive_n = n

    number_of_digits = len(str(positive_n))
    
    result = n * (5 ** number_of_digits)

    return result