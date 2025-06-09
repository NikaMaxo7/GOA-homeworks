def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    
    positive_count = 0
    negative_sum = 0

    for number in arr:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_sum += number
    
    return [positive_count, negative_sum]