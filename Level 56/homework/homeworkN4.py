def even_odd_sort(lst):
    evens = []
    odds = []

    for num in lst:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
            
    return evens + odds