def unique_numbers(lst):
    result = []

    for i in range(len(lst)):
        num = lst[i]
        times = 0

        for j in range(len(lst)):
            if lst[j] == num:
                times = times + 1

        if times == 1:
            result.append(num)

    return result