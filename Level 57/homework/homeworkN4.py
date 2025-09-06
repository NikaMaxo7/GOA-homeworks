students = {
    "Ana": 95,
    "Giorgi": 88,
    "Luka": 76
}

print("Students with score >= 90:")

for name in students:
    if students[name] >= 90:
        print(name, students[name])

students["Nino"] = 100

print("Final students dictionary:", students)