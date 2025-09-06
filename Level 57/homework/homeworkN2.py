fruits = []

for i in range(5):
    fruit = input("Enter favorite fruit " + str(i+1) + ": ")
    fruits.append(fruit)

fruits.append("Mango")
fruits.append("Pineapple")
fruits.pop()

print("Original list:", fruits)

sorted_fruits = fruits[:]
sorted_fruits.sort()

print("Alphabetical order:", sorted_fruits)