a = 5
b = 10
c = 5

result = (a < b) and (b == c) or not (a == c)

# 1) Just like in math, parentheses are evaluated first.
#    Example: (2 + 3) * 4 = do 2 + 3 first, then multiply by 4

# 2) Python also evaluates comparisons inside parentheses first:
#    a < b = 5 < 10 = True
#    b == c = 10 == 5 = False
#    a == c = 5 == 5 → True = but we have "not", so it becomes False

# 3) Now the logical operations:
#    True and False = False
#    False or False = False

# Final result: False

print(result)