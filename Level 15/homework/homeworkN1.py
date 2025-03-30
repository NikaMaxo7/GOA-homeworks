nums = [1,4,3,6,9,11,17,13,26,30]
sum = 0
quantity = 0
for i in nums:
    if i % 2 == 0:
        sum += i
    else:
        quantity += 1
print("Sum=", sum, "Quantity=", quantity)