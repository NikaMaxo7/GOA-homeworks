def undivisible(num, num2):
    res = []
    for i in num:
        if i % num2 == 0:
            res.append(i)
    return res
print(undivisible([1, 23, 165, 2, 3, 92, 10, 34, 911], 3))