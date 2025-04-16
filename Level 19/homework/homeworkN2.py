def larger_sum_list(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    if sum1 > sum2:
        return list1
    else:
        return list2
print(larger_sum_list([2,4,6], [3,5,7]))