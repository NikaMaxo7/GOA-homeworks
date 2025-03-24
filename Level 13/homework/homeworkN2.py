# დაწერეთ პროგრამა რომელიც შემოსულ მთელ რიცხვს 
# გაზრდის ერთით თუ ის კენტია.საბოლოოდ ორივე შემთხვევაში გამობეჭდეთ ეს რიცხვი.

def increase_if_odd(number):
    return number + (number % 2)

number = int(input("enter number: "))

result = increase_if_odd(number)

print(result)
