def delete_nth(order, max_e):
    result = []
    
    for num in order:
        count = 0
        for x in result:
            if x == num:
                count += 1
        if count < max_e:
            result.append(num)
    return result