def remove_smallest(numbers):
    if numbers == []:
        return []

    smallest = min(numbers)

    index_of_smallest = numbers.index(smallest)

    new_list = []

    for i in range(len(numbers)):
        if i != index_of_smallest:
            new_list.append(numbers[i])

    return new_list

# 1) If the list is empty, return an empty list because there's nothing to remove.
# Then, find the smallest number in the list using min().
# Find the index of that smallest number using .index().
# Create a new list.
# Loop through the original list and add all numbers except the one at the index of the smallest number.
# Return this new list.

# 2) Start  
# If list is empty → return empty list  
# Find the smallest number  
# Find the index of the smallest number  
# Create an empty new list  
# For each index i in the list:  
#     If i is not the index of the smallest number → add numbers[i] to the new list  
# Return the new list

# 3) Start  
# ↓  
# Is list empty? → Yes → Return []  
# ↓ No  
# ↓  
# Find smallest number  
# ↓  
# Get index of smallest number  
# ↓  
# Create empty list  
# ↓  
# Loop through each item  
#     ↓  
#     Is index = smallest index?  
#     → Yes → skip  
#     → No → Add item to new list  
# ↓  
# Return new list