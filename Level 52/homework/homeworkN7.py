def decimal_to_binary():
    n = int(input("Enter a decimal number: "))
    
    if n == 0:
        return "Binary: 0"
    
    binary = ""
    
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    return "Binary:", binary

print(decimal_to_binary())