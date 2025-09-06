countries = {}

for i in range(3):
    country = input("Enter country " + str(i+1) + ": ")
    capital = input("Enter capital of " + country + ": ")
    countries[country] = capital

print("Countries and capitals:")

for country in countries:
    print(country, "->", countries[country])

search_country = input("Enter country to search: ")

if search_country in countries:
    print("Capital of", search_country, "is", countries[search_country])
else:
    print("Country not found")