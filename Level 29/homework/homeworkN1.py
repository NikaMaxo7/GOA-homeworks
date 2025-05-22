a = 10
b = 5
c = 7
d = 10

result = (a > b and b < c) or (c == d or a >= d) and not (b == 5)

# 1) a > b = True AND b < c = True AND True = True
# 2) c == d = False OR a >= d = True = False OR True = True
# 3) b == 5 = True
# 4) True OR True AND Not True = True AND True = True
# 5) True OR True = True 
# So result should equal True

print(result)