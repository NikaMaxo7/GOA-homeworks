def get_result_type():
    num1 = input("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ")
    num2 = input("Enter second number: ")

    if "." in num1 or "." in num2:
        num1 = float(num1)
        num2 = float(num2)
    else:
        num1 = int(num1)
        num2 = int(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        return "Invalid operator"

    if type(result) == int:
        return "The result type is: int"
    elif type(result) == float:
        return "The result type is: float"