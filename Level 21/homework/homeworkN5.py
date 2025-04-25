def find_average(nums):
    total = sum(nums)
    count = len(nums)
    if count > 0:
        return total / count
    else:
        return 0