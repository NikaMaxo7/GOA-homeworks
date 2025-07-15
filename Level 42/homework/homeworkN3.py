# 1. for loop + slicing

fruits = ["apple", "banana", "cherry", "mango", "orange"]
for fruit in fruits[:3]:
    print(fruit)

# Result:
# apple
# banana
# cherry


# 2. if statement + slicing

word = "unbelievable"

# Check if it starts with 'un'
if word[:2] == "un":
    print("Word starts with 'un'")


# 3. Passing part of an argument to a function

def process_part(data):
    print("works:", data)

numbers = [1, 2, 3, 4, 5, 6]
process_part(numbers[2:5])


# 4. string reversing slicing

text = "hello"
reversed_text = text[::-1]
print(reversed_text) # output olleh


# 5. list copy slicing

original = [1, 2, 3]
copy = original[:] # creates a copy
copy[0] = 100
print(original) # [1, 2, 3]
print(copy) # [100, 2, 3]