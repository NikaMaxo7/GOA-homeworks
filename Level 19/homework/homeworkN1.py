def combine_and_sort(list1, list2):
    combined = list1 + list2
    combined.sort()
    return combined
print(combine_and_sort([1,4,3,5], [2,7,6,8]))